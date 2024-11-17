# Textra_AI_Research
An intelligent system for analyzing and synthesizing AI research papers. 

## Installation

1. Create a virtual environment:
```python
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate

## Detectron2 Installation on Windows  

Detectron2 does not have official support for Windows, but you can use the following steps to install it:  

### Requirements  
- Windows 10 or later  
- Python ≥ 3.7  
- Visual Studio (Community edition is recommended) for necessary C++ compiler tools.  
- [CUDA](https://developer.nvidia.com/cuda-downloads) and [cuDNN](https://developer.nvidia.com/cudnn) compatible with your version of PyTorch.  

### Steps to Install Detectron2  

1. **Set Up Your Environment:**  
   - It's recommended to use a virtual environment (like `venv` or `conda`) to manage dependencies.  

2. **Install PyTorch and torchvision:**  
   - Run the following command (adjust according to your preferred CUDA version):  
     ```bash  
     pip install torch torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/cu{your_cuda}  
     ```  

3. **Clone the Detectron2 Repository:**  
   ```bash  
   git clone https://github.com/facebookresearch/detectron2.git
4. **Install Detectron2:**

Navigate to the cloned directory:
    ```bash 
        cd detectron2  
5. **Install using pip:**
    ```bash 
        pip install -e .  
