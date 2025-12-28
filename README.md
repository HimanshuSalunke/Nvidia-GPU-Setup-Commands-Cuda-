# Nvidia GPU Setup for TensorFlow & PyTorch (Windows)

Stop wasting time scraping through forums and old StackOverflow posts. If you're trying to get your Nvidia GPU working with both TensorFlow and PyTorch on Windows, this is the exact setup you need.

I put this together so no one else has to struggle with the "DLL load failed" or "Device not found" errors that usually plague this process.

## ⚠️ The Golden Rule: Python 3.10.0 ONLY

Before you do anything else, you **must** have **Python 3.10.0** installed.
Not 3.10.11, not 3.11, and definitely not 3.12.
**Only Python 3.10.0 works.**

You must set this specific version as your **global default** in your Windows Environment Variables.

**Why?**
TensorFlow 2.10 was the last version to support GPU natively on Windows. It is extremely picky. While PyTorch is more flexible, if you want a single environment where you can use **both** libraries (which is pretty common for deep learning projects), **Python 3.10.0 is the strict requirement**.

### 🛑 STOP: Check Your Version First!

Don't guess. Open your terminal (Command Prompt or PowerShell) right now and type:

```bash
python --version
```

If the output is not exactly:
`Python 3.10.0`
**DO NOT PROCEED**.

You need to uninstall other versions or fix your Windows Environment Variables (Path) so that Python 3.10.0 is the one your system uses.

## 🚀 Setup Instructions

Once you've confirmed `python --version` says exactly `3.10.0`, run these commands in your terminal to get everything installed (these specific versions are tested and verified to work together):

```bash
# 1. Update pip just in case
python -m pip install --upgrade pip

# 2. Install generic dependencies
pip install numpy==1.24.4

# 3. Install TensorFlow (The specific version that works on Windows)
pip install tensorflow==2.10.1 keras==2.10.0 h5py==3.7.0 protobuf==3.19.6

# 4. Install PyTorch (CUDA 11.7 compatible)
pip install --user torch==1.13.1+cu117 torchvision==0.14.1+cu117 torchaudio==0.13.1 --extra-index-url https://download.pytorch.org/whl/cu117
```

## 🧪 Verify Your Setup

I've included two scripts in this repo to make sure everything is actually using your GPU.

1.  **Check TensorFlow**:
    Run `python "Check GPU availability for TensorFlow.py"`
    *Should print: "Num GPUs Available: 1" (or more)*

2.  **Check PyTorch**:
    Run `python "pytorch gpu test.py"`
    *Should print: "Using GPU: [Your Card Name]"*

That's it. You're ready to train.
