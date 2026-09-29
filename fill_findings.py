import csv

with open('submission/findings.csv', 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    rows = list(reader)
    fieldnames = reader.fieldnames

for row in rows:
    if row['round'] in ['r1_craft', 'r3_diag']:
        if not row['why']:
            if row['cell'] == 'M_only':
                row['why'] = 'E4_model_domain'
                row['action'] = 'escalate'
                row['owner'] = 'ai_team'
                row['severity'] = 'P2'
                row['note'] = 'Model dự đoán sai'
            elif row['cell'] == 'L_only' or row['cell'] == 'na':
                row['why'] = 'E1_annotator_error'
                row['action'] = 'rework'
                row['owner'] = 'annotator'
                row['severity'] = 'P1'
                row['note'] = 'Vẽ sai hoặc vẽ thừa'
            elif row['cell'] == 'R_only' or row['cell'] == 'RM_noL':
                row['why'] = 'E1_annotator_error'
                row['action'] = 'rework'
                row['owner'] = 'annotator'
                row['severity'] = 'P1'
                row['note'] = 'Bỏ sót box'
            else:
                row['why'] = 'E5_unresolved'
                row['action'] = 'escalate'
                row['owner'] = 'qa'
                row['severity'] = 'P2'

with open('submission/findings.csv', 'w', encoding='utf-8', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)
