import os
import time
print("Starting Deployment!")
time.sleep(5)
os.system("curl -Lo memfix.zip https://github.com/nolanaatama/microsoftexcel/raw/main/memfix.zip")
os.system("unzip /content/memfix.zip")
os.system("apt -y update -qq")
os.system("env LD_PRELOAD=/content/libtcmalloc_minimal.so.4")
os.system("curl -Lo microsoftexcel.zip https://huggingface.co/nolanaatama/colab/resolve/main/microsoftexcel151.zip")
os.system("unzip /content/microsoftexcel.zip")
os.system("git clone https://github.com/nolanaatama/microsoftexcel-tunnels /content/microsoftexcel/extensions/microsoftexcel-tunnels")
os.system("git clone https://github.com/nolanaatama/microsoftexcel-controlnet /content/microsoftexcel/extensions/microsoftexcel-controlnet")
os.system("git clone https://github.com/fkunn1326/openpose-editor /content/microsoftexcel/extensions/openpose-editor")
os.system("git clone https://github.com/nolanaatama/microsoftexcel-3d-open-pose-editor /content/microsoftexcel/extensions/microsoftexcel-3d-open-pose-editor")
os.system("git clone https://github.com/nolanaatama/a1111-microsoftexcel-tagcomplete /content/microsoftexcel/extensions/a1111-microsoftexcel-tagcomplete")
os.system("git clone https://github.com/nolanaatama/a1111-microsoftexcel-locon /content/microsoftexcel/extensions/a1111-microsoftexcel-locon")
os.system("mkdir /content/microsoftexcel/models/ESRGAN")
os.system("curl -Lo /content/microsoftexcel/extensions/microsoftexcel-images-browser.zip https://huggingface.co/nolanaatama/colab/resolve/main/microsoftexcel-images-browser.zip")
os.system("curl -Lo /content/microsoftexcel/embeddings/embeddings.zip https://huggingface.co/nolanaatama/colab/resolve/main/embeddings.zip")
os.system("curl -Lo /content/microsoftexcel/models/ESRGAN/upscalers.zip https://huggingface.co/nolanaatama/colab/resolve/main/upscalers.zip")
os.system("cd /content/microsoftexcel/extensions")
os.system("unzip /content/microsoftexcel/extensions/microsoftexcel-images-browser.zip")
os.system("cd /content/microsoftexcel/embeddings")
os.system("unzip /content/microsoftexcel/embeddings/embeddings.zip")
os.system("cd /content/microsoftexcel/models/ESRGAN")
os.system("unzip /content/microsoftexcel/models/ESRGAN/upscalers.zip")
os.system("rm upscalers.zip")
os.system("cd /content")
os.system("curl -Lo /content/microsoftexcel/models/Stable-diffusion/meinamix.safetensors https://huggingface.co/nolanaatama/mnmx/resolve/main/mnmx.safetensors")
os.system("rm microsoftexcel.zip")
os.system("cd /content/microsoftexcel")
os.system("COMMANDLINE_ARGS=\"--share --disable-safe-unpickle --no-half-vae --xformers --enable-insecure-extension --gradio-queue\" REQS_FILE=\"requirements.txt\" python launch.py")
