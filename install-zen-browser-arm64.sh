STARTDIR=$(pwd)
# check sudo 
if [ "$EUID" -ne 0 ]
  then echo "Please run as root"
  exit
fi

echo "Creating Temp Directory in /tmp/zen-browser-install ..."

TEMPDIR=/tmp/zen-browser-install
mkdir -p $TEMPDIR
cd $TEMPDIR


echo "Downloading Zen Browser Install Files ..."

curl -L https://github.com/ArchitektApx/zen-browser-arm64-copr/archive/refs/heads/master.zip -o master.zip
curl -L https://github.com/ArchitektApx/zen-browser-arm64-copr/releases/download/1.0.1-a.19/zen.linux-generic.tar.bz2

echo "Extracting Zen Browser Install Files ..."

unzip -q master.zip
tar xjf zen.linux-generic.tar.bz2 

echo "Installing Zen Browser to /opt/zen-browser ..."

mkdir -p /opt/zen-browser
mkdir -p /opt/zen-browser/distribution
mkdir -p /usr/share/icons/hicolor/16x16/apps
mkdir -p /usr/share/icons/hicolor/32x32/apps
mkdir -p /usr/share/icons/hicolor/48x48/apps
mkdir -p /usr/share/icons/hicolor/64x64/apps
mkdir -p /usr/share/icons/hicolor/128x128/apps
cp -rf zen/* /opt/zen-browser/
install -m755 zen-browser-arm64-copr-master/zen-browser /usr/bin/zen-browser
install -m755 zen-browser-arm64-copr-master/zen-browser.desktop "/usr/share/applications/zen-browser.desktop"
install -m444 zen-browser-arm64-copr-master/policies.json "/opt/zen-browser/distribution/policies.json"
for i in 16x16 32x32 48x48 64x64 128x128; do
    install -m755 /opt/zen-browser/browser/chrome/icons/default/default${i/x*}.png /usr/share/icons/hicolor/$i/apps/zen-browser.png
done
# system provided dictionaries
if [ -d /usr/share/hunspell ]; then ln -Tsf /usr/share/hunspell /opt/zen-browser/dictionaries 
fi
if [ -d /usr/share/hyphen ]; then ln -Tsf /usr/share/hyphen /opt/zen-browser/hyphenation
fi

echo "Cleaning Up ..."

cd $STARTDIR
rm -rf $TEMPDIR

echo "Done! Zen Browser is installed."
echo "You can now run Zen Browser by typing zen-browser in the terminal"
echo "or by searching for it in your applications menu."
