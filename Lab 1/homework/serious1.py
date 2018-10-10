import schedule
import time

def job():
    from gmail import GMail, Message
    import random

    gmail = GMail('zoey.techkids@gmail.com','techkids')

    symptom_dictionary = {
        'đau bụng':'dạ dày',
        'đau chân':'xương khớp',
        'mệt mỏi':'ung thư',
    }

    html_template = '''
    <p>Ch&agrave;o sếp</p>
    <p><strong>S&aacute;ng nay</strong> em {{ symptom }} qu&aacute;. Chắc l&agrave; em bị {{ disease }} rồi&nbsp;</p>
    <p><span style="color: #993366;">Cho em xin nghỉ ahuhu</span></p>
    <p>&nbsp;</p>
    '''

    #get random symptom and disease
    symp_disease = []
    symp_disease = random.choice(list(symptom_dictionary.items()))
    html_content = html_template.replace("{{ symptom }}",symp_disease[0])
    html_content = html_content.replace("{{ disease }}",symp_disease[1])

    msg = Message('This is Yen',to='zoey.techkids@gmail.com',html=html_content,attachments=[])

    gmail.send(msg)
    return schedule.cancel_job
    
schedule.every().day.at("7:01").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)