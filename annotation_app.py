# USING JSON DIRECTLY ----------------------------------------------------------------

# import streamlit as st 
# import json 

# # Data loading
# with open("Final dataset/law_nondup copy 12 annotation.json", "r", encoding="utf-8") as f:
#     legal_corpus = json.load(f)
# with open("Final dataset/question_9.91 annotation.json", "r", encoding="utf-8") as f:
#     qa_data = json.load(f)


# def display_qa_entity(entity):
#     st.write(f"**ID:** {entity['id']}")
#     st.write(f"**Link:** {entity['href']}")
#     st.write(f"**Question:** {entity['question']}")
#     st.write(f"**Answer:** {entity['answer']}")
#     st.write("**Relevant laws:**")
#     for law in entity['relevant_laws']:
#         st.write(f"- [{law['name']}]({law['href']})")

# def display_legal_entity(entity):
#     st.write(f"**ID:** {entity['id']}")
#     st.write(f"**Link:** {entity['href']}")
#     st.write(f"**Title:** {entity['title']}")
#     st.write("**Content:**")
#     for chapter in entity['content']:
#         st.write(f"**{chapter['title_Chapter']}**")
#         for section in chapter['content_Chapter']:
#             st.write(f"{section['title_Section']}")
#             for article in section['content_Section']:
#                 st.write(f"{article['content_Article']}")

# def main():
#     st.sidebar.title("Navigation")

#     st.title("Data")

#     # Get user input
#     dataset_choice = st.sidebar.radio("Choose Dataset:", ["QA Data", "Legal Corpus"])

#     if dataset_choice == "QA Data":
#         entity_index = st.sidebar.number_input("Enter entity number:", min_value=1, max_value=len(qa_data), value=1)
#         entity = qa_data[entity_index - 1]
#         display_qa_entity(entity)
#         entity_type = "QA Data"
#         entity_id = entity['id']
#         entities_count = len(qa_data)
#     else:
#         entity_index = st.sidebar.number_input("Enter entity number:", min_value=1, max_value=len(legal_corpus), value=1)
#         entity = legal_corpus[entity_index - 1]
#         display_legal_entity(entity)
#         entity_type = "Legal Corpus"
#         entity_id = entity['id']
#         entities_count = len(legal_corpus)

#     # Counter
#     st.sidebar.markdown(f"### Entity Count: {entity_index}/{entities_count}")
    
#     st.markdown("---")
#     st.title("Annotation")

#     # Check if annotation exists
#     if 'annotation_label' in entity:
#         st.write(f"**Current label:** {entity['annotation_label'] or 'No label set.'}")
#         st.write(f"**Current reasoning:** {entity['labeling_reason'] or 'No reasoning provided.'}")
#     else:
#         st.write("Haven't been checked or annotated.")

#     st.markdown("---")

#     # Annotation label
#     annotation_label = st.selectbox("Annotation label:", ["True", "False", "Other"])

#     # Label reasoning
#     label_reasoning = st.text_area("Label reasoning:")

#     # Save button
#     if st.button("Save"):
#         # Update the entity with annotation label and reasoning
#         entity['annotation_label'] = annotation_label
#         entity['labeling_reason'] = label_reasoning

#         # Save the updated data to the file
#         if entity_type == "QA Data":
#             with open("Final dataset/question_9.91 annotation.json", "w", encoding="utf-8") as f:
#                 json.dump(qa_data, f, ensure_ascii=False, indent=4)
#         else:
#             with open("Final dataset/law_nondup copy 12 annotation.json", "w", encoding="utf-8") as f:
#                 json.dump(legal_corpus, f, ensure_ascii=False, indent=4)

#         st.success("Annotation saved successfully!")

# if __name__ == "__main__":
#     main()







# USING MONGODB ----------------------------------------------------------------
# Name: User, Password: verystrongpassword -> Access database




import streamlit as st
import pymongo
import json
import time

# Connect to MongoDB
client = pymongo.MongoClient("mongodb+srv://User:verystrongpassword@ner.0oq3pys.mongodb.net/")  # Update the connection string with your MongoDB URI
db = client["annotation_dataset"]  # Replace 'your_database_name' with your actual database name
qa_collection = db["qa_dataset"]  # Replace 'your_qa_collection' with your actual collection name
legal_collection = db["legal_corpus"]  # Replace 'your_legal_collection' with your actual collection name

# Static search since no need to update, code is below 

# ----Choice 1: Using in MongoDB (Slower but more privacy)
# corpus_reformated_collection = db["corpus_reformated"]
# corpus_list = list(corpus_reformated_collection.find({})) #cursor to find, then change it to LIST (vi neu de nguyen cursor thi chay dc 1 lan relevant law)

# ----Choice 2: Using JSON (Faster but less privacy)
with open('dataset/corpus_reformated.json', 'r', encoding='utf-8') as file:
    corpus_list = json.load(file)
# Since the file is big -> Use Git LFS
# Add .gitattributes, install...
# Luc dung git nho git lfs track ".json"

# relevant_laws = []

# for item in data:
#     id_law = item['id']
#     title = item['title']
#     content = item['content']
#     for chapter in content:
#         id_chapter = chapter['id_Chapter']
#         for section in chapter['content_Chapter']:
#             id_section = section['id_Section']
#             for article in section['content_Section']:
#                 id_article =  article['id_Article']
#                 content_article = article['content_Article']

#                 full_name = f"{title} (Chương {id_chapter} Mục {id_section} Điều {id_article})"
#                 relevant_laws.append(
#                     {'title': title, 
#                         'full_name': full_name,
#                         'id_Law': id_law,
#                         'id_Chapter': id_chapter,
#                         'id_Section': id_section,
#                         'id_Article': id_article,
#                         'content_Article': content_article}
#                         )


# Function to check if the labeler name is correct
def check_labeler(annotator_name):
    # List of correct labeler names
    correct_annos = ["khoi", "anno1", "anno2", "anno3", "anno4", "anno5", "anno6", "anno7", "anno8", "anno9", "anno10"]  # Update with correct labeler names
    return annotator_name in correct_annos

def display_qa_entity(entity):
    st.write(f"**ID:** {entity['id']}")
    # st.write(f"**Link:** {entity['href']}")  # For privacy
    st.write(f"**Câu hỏi:** {entity['question']}")
    st.write(f"**Câu trả lời:** {entity['answer']}")
    st.write("**Điều luật liên quan:**")
    content_law = []
    for law in entity['relevant_laws']:
        # st.write(f"- [{law['name']}]({law['href']})") # For privacy
        st.write(f"- {law['name']}")
        id_law = law['id_Law']
        id_chapter = law['id_Chapter']
        id_section = law['id_Section']
        id_article = law['id_Article']
        # print(id_law, id_chapter, id_section, id_article)
        for e in corpus_list:
            if e['id_Law'] == id_law and e['id_Chapter'] == id_chapter and e['id_Section'] == id_section and e['id_Article'] == id_article:
                content_law = e['content_Article']
                # print(content_law)
                st.write(f"**Nội dung điều luật:** {content_law}")
                st.write("---")

        # # Lazy loading: Fetch documents from the database in batches
        # batch_size = 1000  # Adjust the batch size as needed
        # skip = 0
        # batch = corpus_reformated_collection.find({}).skip(skip).limit(batch_size)
        # while batch.alive:
        #     for e in batch:
        #         if e['id_Law'] == id_law and e['id_Chapter'] == id_chapter and e['id_Section'] == id_section and e['id_Article'] == id_article:
        #             content_law = e['content_Article']
        #             print(content_law)
        #             st.write(f"**Content:** {content_law}")
        #             st.write("---")
        #     skip += batch_size
        #     batch = corpus_reformated_collection.find({}).skip(skip).limit(batch_size)
        
                

def display_legal_entity(entity):
    st.write(f"**ID:** {entity['id']}")
    st.write(f"**Link:** {entity['href']}")
    st.write(f"**Tiêu đề:** {entity['title']}")
    st.write("**Content:**")
    for chapter in entity['content']:
        st.write(f"**{chapter['title_Chapter']}**")
        for section in chapter['content_Chapter']:
            st.write(f"{section['title_Section']}")
            for article in section['content_Section']:
                st.write(f"{article['content_Article']}")

# Function to display a list of relevant laws for selection
#--------------------OLD - slower?--------------------------------------------
def display_and_get_new_relevant_laws():
    # corpus_id_list o file json o tren
    selected_laws = st.multiselect("Chọn điều luật liên quan đúng (nếu cần thay đổi):", [law["full_name"] for law in corpus_list])

    return [law for law in corpus_list if law["full_name"] in selected_laws]

#----------------------NEW - faster (khoảng 1s giữa các relevant law vs nhau thôi) --------------------------------
# # Define a global variable to keep track of the current index for lazy loading
# current_index = 0

# # Function to load the next chunk of relevant laws
# def load_next_chunk(chunk_size):
#     global current_index
#     next_chunk = corpus_list[current_index:current_index + chunk_size]
#     current_index += chunk_size
#     return next_chunk

# # Function to display and get new relevant laws (with lazy loading)
# # @st.cache_data(experimental_allow_widgets=True)
# def display_and_get_new_relevant_laws():
#     chunk_size = 1000  # Adjust the chunk size as needed
#     selected_laws = st.multiselect("Chọn điều luật liên quan đúng (nếu cần thay đổi):", [law["full_name"] for law in load_next_chunk(chunk_size)])
#     return [law for law in corpus_list if law["full_name"] in selected_laws]

def main():
    st.sidebar.title("Thanh điều hướng")

    # Get user input for labeler name
    annotator_name = st.sidebar.text_input("Điền tên người chấm tại đây:", max_chars=100)
    
    if check_labeler(annotator_name):
        st.sidebar.markdown("Tên người chấm hợp lệ.")
        # Continue with the rest of the application

        st.title("Dữ liệu")

        # Get user input
        # dataset_choice = st.sidebar.radio("Choose Dataset:", ["QA Data", "Legal Corpus"])
        dataset_choice = st.sidebar.radio("Chọn Bộ dữ liệu:", ["Dữ liệu QA"])

        if dataset_choice == "Dữ liệu QA":
            entity_index = st.sidebar.number_input("Điền số thứ tự câu hỏi:", min_value=1, max_value=qa_collection.count_documents({}), value=1)
            entity = qa_collection.find_one({}, skip=entity_index - 1)
            display_qa_entity(entity)
            entity_type = "QA Data"
            entity_id = entity['id']
            entities_count = qa_collection.count_documents({})
        else:
            entity_index = st.sidebar.number_input("Điền số thứ tự câu hỏi:", min_value=1, max_value=legal_collection.count_documents({}), value=1)
            entity = legal_collection.find_one({}, skip=entity_index - 1)
            display_legal_entity(entity)
            entity_type = "Legal Corpus"
            entity_id = entity['id']
            entities_count = legal_collection.count_documents({})

        # Counter
        st.sidebar.markdown(f"### Số thứ tự câu hỏi: {entity_index}/{entities_count}")
        

        # Display THE LATEST annotation (REMOVED!)
        # st.title("Annotation")

        # # Check if annotation exists
        # if 'annotation_label' in entity:
        #     st.write(f"**Latest label:** {entity['annotation_label'] or 'No label set.'}")
        #     st.write(f"**Latest reasoning:** {entity['labeling_reason'] or 'No reasoning provided.'}")
        #     st.write(f"**Latest labeler:** {entity['labeler'] or 'No labeler has checked.'}")
        # else:
        #     st.write("Haven't been checked or annotated.")

        # st.markdown("---")

    
        # Annotation ANSWER
        st.title("Đánh giá Câu trả lời")
        annotator_answer_label = st.selectbox("Nhãn câu trả lời của người chấm:", ["Đúng", "Sai"])
        annotator_answer_feedback = st.text_area("Nhận xét về câu trả lời:")

        st.markdown("---")

        # Annotation RELEVANT LAWS
        st.title("Đánh giá Điều luật liên quan")
        annotator_relevant_laws_label = st.selectbox("Nhãn điều luật liên quan của người chấm:", ["Đúng", "Sai"])
        annotator_relevant_laws_feedback = st.text_area("Nhận xét về điều luật liên quan:")

        # New relevant law (if false)
        if entity_type == "QA Data":
            annotator_new_relevant_laws = display_and_get_new_relevant_laws()

        # Save button
        if st.button("Save"):
            # Update the document in MongoDB
            if entity_type == "QA Data":
                item = {
                    'annotator_answer_label': annotator_answer_label,
                    'annotator_answer_feedback': annotator_answer_feedback,
                    'annotator_relevant_laws_label': annotator_relevant_laws_label,
                    'annotator_relevant_laws_feedback': annotator_relevant_laws_feedback,
                    'annotator_new_relevant_laws': annotator_new_relevant_laws,
                    'annotator_name': annotator_name
                }
               
                # qa_collection.replace_one({"_id": entity["_id"]}, entity)
                qa_collection.update_one({"_id": entity["_id"]}, {"$push": {"annotation_list": item}})
            else:
                # -----------------------------------------------
                # Chưa sửa đoạn này!!!!!!!!!!!!!!!!!!! Ms chỉ update vs format lại chuẩn qa_collection
                # -----------------------------------------------

                legal_collection.replace_one({"_id": entity["_id"]}, entity)

            st.success("Lưu lai thành công!")
    

    else:
        st.sidebar.markdown("Tên người chấm không hợp lệ.")

if __name__ == "__main__":
    main()

