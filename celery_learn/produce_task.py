from celery_learn.tasks import send_email

result = send_email.delay('yuan')
print(result.id)
result2 = send_email.delay('alex')
print(result2.id)  # 更加id值查看结果