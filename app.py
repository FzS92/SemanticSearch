import torch
import gradio as gr
from torch.nn.functional import cosine_similarity
from sentence_transformers import SentenceTransformer


def remove_extra_newlines(string):
    return "\n".join(line for line in string.splitlines() if line.strip())


def separate_paragraphs(text):
    paragraphs = text.split("\n")
    return paragraphs


def encode_text(text, model):
    # Forward pass through the model
    with torch.no_grad():
        outputs = model.encode(text)
        outputs = torch.tensor(outputs)
    return outputs


def get_top_n_cosine_similarity_rows(tensor1, tensor2, n):
    # Calculate cosine similarity between the two tensors
    similarity_scores = cosine_similarity(tensor1, tensor2)
    # Get the top N indices with highest similarity scores
    top_n_indices = torch.topk(similarity_scores.squeeze(), n)[1]
    return top_n_indices


# Example usage
text_example = """The Internet of Things (IoT) is a network of interconnected devices that exchange data and communicate with each other. It encompasses various objects embedded with sensors, software, and connectivity capabilities. The IoT has transformed many industries and opened up new opportunities for businesses.

In the healthcare sector, the IoT is revolutionizing patient care. Connected devices such as wearables and medical sensors collect real-time data on patients' vital signs and health conditions. This information can be shared with healthcare providers, allowing for remote monitoring and early detection of health issues.

Smart homes are another area where the IoT is making a significant impact. Connected devices like thermostats, security systems, and appliances can be controlled remotely through smartphone apps. This enables homeowners to monitor and manage their homes' energy usage, security, and other aspects conveniently.

The manufacturing industry is leveraging the IoT to improve operational efficiency. Smart factories use sensors and automation to collect and analyze data in real-time, optimizing production processes and minimizing downtime. This leads to increased productivity and cost savings.

Transportation is also benefiting from IoT advancements. Connected vehicles can communicate with traffic infrastructure, providing real-time information on traffic conditions and optimizing routes. This improves road safety, reduces congestion, and enhances the overall transportation experience.

In agriculture, the IoT is transforming traditional farming practices. Connected sensors and monitoring systems enable farmers to gather data on soil moisture, temperature, and crop health. This data-driven approach helps optimize irrigation, reduce resource wastage, and improve crop yields.

Retail is another sector experiencing the impact of the IoT. Connected devices, such as beacons and RFID tags, enable retailers to track inventory levels, monitor customer behavior, and personalize shopping experiences. This facilitates efficient supply chain management and targeted marketing strategies.

The energy sector is embracing the IoT to improve energy efficiency and sustainability. Smart grids and connected energy management systems allow for better monitoring and control of energy consumption. This leads to optimized energy distribution, reduced wastage, and increased reliance on renewable sources.

Overall, the Internet of Things is driving innovation and transforming various industries. Its ability to connect and collect data from diverse sources enables smarter decision-making, improved efficiency, and enhanced user experiences. As the IoT continues to evolve, we can expect further advancements and integration into our everyday lives."""

searching_for_example = "IoT in healthcare"

# Inputs
model_name = gr.Textbox(
    value="all-mpnet-base-v2", label="Encoder model (See the code)"
)  # find the list here: https://www.sbert.net/docs/pretrained_models.html
searching_for = gr.Textbox(value=searching_for_example, label="Semantic search for")
text = gr.Textbox(value=text_example, label="Your main text")

# outputs
out = gr.Textbox(
    value="Press submit", label="Top five paragraphs that share similar meaning"
)


def semantic_search(model_name, searching_for, text):
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model = SentenceTransformer(model_name).to(device)

    text = remove_extra_newlines(text)
    text = separate_paragraphs(text)
    searching_for = remove_extra_newlines(searching_for)
    search_and_text = [searching_for]
    search_and_text.extend(text)

    encoded = encode_text(search_and_text, model)

    encoded_search = encoded[0]  # Encode of searching_for
    encoded_text = encoded[1:]  # Encode of text

    n_similar_texts = 5  # 5 top search results
    n_similar_texts = min(n_similar_texts, len(text))

    index_of_similar = get_top_n_cosine_similarity_rows(
        encoded_search, encoded_text, n_similar_texts
    )

    output = f"Top {n_similar_texts} are as follows:\n\n"
    for i in range(n_similar_texts):
        output += f"Match number {i+1}:\n"
        output += text[index_of_similar[i]] + "\n\n"

    return output


iface = gr.Interface(
    fn=semantic_search,
    title="Semantic Search",
    inputs=[model_name, searching_for, text],
    outputs=[out],
)

iface.launch(share=False)
