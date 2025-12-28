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

I have prepared a separate file with all the necessary installation commands. Even the **CUDA installation** is handled within these commands (via strict versioning and included binaries), so you don't need to manually hunt for drivers.

**👉 Open [Setup Commands.txt](Setup%20Commands.txt) and run the commands listed there.**

These commands cover:
1.  Upgrading pip.
2.  Installing key dependencies (NumPy).
3.  Installing the specific TensorFlow version (2.10.1) that supports GPU on Windows.
4.  Installing the compatible PyTorch version (includes CUDA 11.7 binaries).

## 💡 Important: Working with Virtual Environments

If you create a virtual environment for your project (which you should!), **you must repeat the setup steps inside that environment.**

When you create a new environment (e.g., `python -m venv myenv`), it starts **empty**. It does NOT inherit the global packages you might have installed on your main system.

1.  Create the environment using Python 3.10: `python -m venv myenv`
2.  Activate it: `.\myenv\Scripts\activate`
3.  **Run the commands from `Setup Commands.txt` again.**

If you skip this, your project will not detect the GPU, because the libraries live in the global space, not inside your new isolated environment.

## 🧪 Verify Your Setup.

I've included two scripts in this repo to make sure everything is actually using your GPU.

1.  **Check TensorFlow**:
    Run `python "Check GPU availability for TensorFlow.py"`
    *Should print: "Num GPUs Available: 1" (or more)*

2.  **Check PyTorch**:
    Run `python "pytorch gpu test.py"`
    *Should print: "Using GPU: [Your Card Name]"*

That's it. You're ready to train.
