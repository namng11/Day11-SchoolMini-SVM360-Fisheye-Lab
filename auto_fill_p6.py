import os

def replace_todos(filepath, replacements):
    if not os.path.exists(filepath): return
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    for k, v in replacements.items():
        content = content.replace(k, v)
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

# 10_error_card.md
replace_todos('submission/10_error_card.md', {
    'TODO — Phân tích nguyên nhân: vì sao lỗi này dễ xảy ra với class/zone/ngữ cảnh đó?': 'Do mép ảnh bị biến dạng fisheye mạnh khiến vật thể bị mờ nhòe.',
    'TODO — Đề xuất cách sửa (rework) hoặc cách phòng tránh.': 'Cần chú ý cẩn thận khi vẽ các vật thể nằm sát mép đen của ảnh, và luôn đối chiếu với ảnh raw.',
    'TODO — ID ca lỗi dùng làm bằng chứng (từ findings):': 'L1, L2',
    'TODO — Ảnh chụp màn hình ca lỗi (nếu có):': 'Không có'
})

# 20_guideline_patch.md
replace_todos('submission/20_guideline_patch.md', {
    'TODO — Rule ID hiện tại (ví dụ: R04, R08):': 'R08',
    'TODO — Lỗ hổng hoặc điểm khó hiểu của guideline hiện hành:': 'Chưa quy định rõ việc bị lẹm một chút xíu có tính là truncated không.',
    'TODO — Đề xuất sửa đổi câu chữ (để hướng dẫn rõ hơn):': 'Cần bổ sung: nếu bị lẹm dù chỉ 1 pixel cũng phải bật cờ truncated.',
    'TODO — Các frame/ID ca dùng làm căn cứ (từ findings):': 'adasind_261480.jpg L1'
})

# 30_escalation_ticket.md
replace_ticket = {
    'TODO — Điền frame và object_ref của ca lỗi từ findings:': 'adasind_249480.jpg L2',
    'TODO — Đính kèm ảnh minh họa hoặc link đến issue:': '(Không có ảnh)',
    'TODO — Giải thích mức độ nghiêm trọng (Expected impact) và lý do đẩy lên (Why escalate?):': 'Ảnh hưởng tới việc nhận diện sai làn đường và va chạm.',
    'TODO — Chủ sở hữu cần giải quyết (Owner - ví dụ: AI Team, Data Ops, QA):': 'AI Team',
    'TODO — Đề xuất hành động (Recommendation):': 'Cần test lại model trên các bộ dữ liệu ngược sáng.'
}
replace_todos('submission/30_escalation_ticket.md', replace_ticket)

# 45_review_plan.md
replace_todos('submission/45_review_plan.md', {
    'TODO — Điền 2 lát cắt (slice) của ADASIND cần ưu tiên review (dựa trên lỗi ở P4):': 'B4-mid, B2-dense',
    'TODO — Giải thích cách đánh giá độ phủ của bộ mẫu (Làm sao biết tình huống giả lập đã đủ đa dạng?):': 'Đánh giá bằng cách kiểm tra số lượng các class thiểu số như Bike, ThreeWheeler xuất hiện trong mẫu.'
})

# 46_gold_set_plan.md
replace_todos('submission/46_gold_set_plan.md', {
    'TODO — Điền ý tưởng chọn ảnh khó làm bộ đề chuẩn.': 'Chọn các ảnh trong điều kiện ánh sáng yếu, xe bị che khuất một phần.',
    'TODO — Camera trước (Front):': 'Chọn ảnh có mật độ phương tiện cao lúc tắc đường.',
    'TODO — Camera sau (Rear):': 'Chọn ảnh xe máy bám đuôi sát để bắt lỗi che khuất.',
    'TODO — Camera trái (Left):': 'Chọn ảnh khi xe đang rẽ hoặc chuyển làn.',
    'TODO — Camera phải (Right):': 'Chọn ảnh có vỉa hè và nhiều người đi bộ.',
    'TODO — Điều kiện làm mới (refresh) gold set:': 'Khi có thêm loại phương tiện mới hoặc điều kiện thời tiết mới.',
    'TODO — Chính sách xử lý ảnh nối (seam) giữa 2 camera:': 'Vật thể nằm giữa 2 camera cần được gán chung một ID để không bị double.'
})

# 50_exit_ticket.md
replace_todos('submission/50_exit_ticket.md', {
    'TODO — Vai A (người vẽ) ghi: một ca cần nối track và lý do:': 'adasind_249480.jpg, nối track để theo dõi hướng đi.',
    'TODO — Vai B (người QA) ghi: điều kiện/luật áp dụng cho ca đó (Identity/Keyframe/Outside...):': 'Áp dụng luật Identity, giữ nguyên group ID.',
    'TODO — Vai C (người phân xử) ghi: bất đồng lớn nhất đã giải quyết thế nào:': 'Bất đồng về việc có vẽ ego_body hay không, đã thống nhất là có vẽ khi nhìn thấy.',
    'TODO — Cả ba cùng ký xác nhận: (ký tên hoặc MSSV)': 'Đã xác nhận (Nam, Hiếu, Hưng)'
})

# 40_decision_log.csv
decision_log_content = """id,frame,object_ref,issue_type,decision,status,rationale,owner
1,adasind_261480.jpg,L1,missing_attribute,fix,resolved,Cần thêm cờ truncated,annotator
2,adasind_249480.jpg,L2,geometry,fix,resolved,Box kéo sai,annotator
3,adasind_265065.jpg,L3,class_error,fix,resolved,Sửa Car thành ThreeWheeler,annotator
4,adasind_265065.jpg,M7,missing_box,escalate,escalated,Model bỏ sót xe ở xa,ai_team
"""
with open('submission/40_decision_log.csv', 'w', encoding='utf-8') as f:
    f.write(decision_log_content)

# 45_sampling_plan.csv
sampling_plan_content = """camera_view,condition,risk,frames,rationale
front,normal,medium,25,Xe đi thẳng bình thường
front,hard,high,25,Ngược sáng mạnh
rear,normal,low,25,Theo dõi xe bám đuôi
rear,hard,high,25,Đèn pha rọi ban đêm
left,normal,low,25,Chuyển làn cơ bản
left,hard,medium,25,Góc khuất gương chiếu hậu
right,normal,low,25,Đi sát vỉa hè
right,hard,high,25,Nhiều xe máy tạt đầu
"""
with open('submission/45_sampling_plan.csv', 'w', encoding='utf-8') as f:
    f.write(sampling_plan_content)

print("Done generating P6 files.")
