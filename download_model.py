import os
import requests
import sys

# اسم المجلد اللي حيتحفظ فيه الموديل
MODEL_DIR = "model"
# اسم ملف الموديل
MODEL_FILE = "ggml-model.bin"

# رابط الموديل الرسمي من Hugging Face
MODEL_URL = "https://huggingface.co/TheBloke/GPT4All-13B-snoozy-GGML/resolve/main/GPT4All-13B-snoozy.ggmlv3.q2_K.bin"

# إنشاء المجلد لو ما موجود
os.makedirs(MODEL_DIR, exist_ok=True)

# مسار الموديل النهائي
model_path = os.path.join(MODEL_DIR, MODEL_FILE)

# لو الموديل موجود ما ينزل تاني
if os.path.exists(model_path):
    print(f"الموديل موجود بالفعل: {model_path}")
    sys.exit(0)

# تنزيل الموديل مع عرض تقدم التحميل
print(f"جاري تنزيل الموديل من {MODEL_URL} ...")
response = requests.get(MODEL_URL, stream=True)

total_length = response.headers.get('content-length')
if total_length is None:
    # بدون طول محدد
    with open(model_path, 'wb') as f:
        f.write(response.content)
else:
    total_length = int(total_length)
    downloaded = 0
    chunk_size = 8192
    with open(model_path, 'wb') as f:
        for data in response.iter_content(chunk_size=chunk_size):
            f.write(data)
            downloaded += len(data)
            done = int(50 * downloaded / total_length)
            sys.stdout.write("\r[%s%s] %d%%" % ('#' * done, '.' * (50 - done), 100 * downloaded / total_length))
            sys.stdout.flush()
    print("\nتم التحميل بنجاح!")