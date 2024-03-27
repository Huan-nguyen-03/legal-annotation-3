Bộ dữ liệu bao gồm 2 file:

I. Question dataset:
1. Mô tả:
Các trường trong question dataset:
- id.
- href: Đường dẫn đến trang web tvpl chứa câu hỏi.
- question: Câu hỏi.
- answer: Câu trả lời.
- relevant_laws: Các văn bản luật liên quan đến việc trả lời câu hỏi đó. Bao gồm các thông tin như sau:
    + name.
    + href: đường dẫn đến văn bản luật tvpl.
    + id_Law: số hiệu văn bản luật.
    + id_Chapter: id của chương chứa điều luật liên quan (id này được lấy dựa vào bộ Legal dataset).
    + id_Section: id của mục chứa điều luật liên quan.
    + id_Article: id của điều luật liên quan.

2. Các trường cần kiểm tra lại:
- answer: kiểm tra xem câu trả lời có đúng không?
- relevant_laws: kiểm tra xem các điều luật liên quan có đúng, đầy đủ không?


II. Legal dataset: 
1. Mô tả:
Các trường trong legal dataset:
- id: số hiệu văn bản luật.
- href: đường dẫn đến văn bản luật tvpl.
- title: tên văn bản luật.
- content: nội dung văn bản luật, được xây dựng theo phân cấp từ lớn đến nhỏ lần lượt là Chương (Chapter), Mục (Section), Điều (Article).
- id_Chapter, id_Section, id_Article: id tương ứng của Chương, Mục, Điều.
- title_Chapter, title_Section: tên của Chương, Mục.
- content_Chapter, content_Section, content_Article: nội dung của Chương, Mục, Điều.

2. Các trường cần kiểm tra lại.
Kiểm tra tính đúng đắn và đầy đủ của mỗi văn bản luật.