# Create virtual environment
> python3 -m venv .venv

>source .venv/bin/activate

# Install Homebrew (if not already installed):
> /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

> sudo chown -R dgaidar /usr/local/share/zsh /usr/local/share/zsh/site-functions

> brew install tcl-tk


# Install required modules
> pip install -r requirements.txt

python -m ensurepip --upgrade
python -m pip install --upgrade pip
pip install pymupdf pillow
pip install PyMuPDF
pip install opencv-python
#pip install Pillow
