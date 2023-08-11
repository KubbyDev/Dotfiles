cd $HOME/Code/Linux/Config

# Puts the current files in tmp to avoid
# deleting them by accident
trash $HOME/.vimrc
trash $HOME/.bash_aliases
trash $HOME/.bashrc
trash $HOME/.zshrc

dos2unix vimrc
dos2unix zshrc
dos2unix bash_aliases
dos2unix bashrc

cp vimrc $HOME/.vimrc
cp bash_aliases $HOME/.bash_aliases
cp bashrc $HOME/.bashrc
cp zshrc $HOME/.zshrc
