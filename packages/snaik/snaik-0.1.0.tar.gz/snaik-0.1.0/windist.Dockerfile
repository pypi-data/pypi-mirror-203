# Main dockerfile is from unix, windows is solely provided for building .exe artifacts
FROM tobix/pywine:3.10 as compile

COPY . /snaik
WORKDIR /snaik

# Install dependencies
RUN wine python --version
RUN wine pip install --no-cache-dir -r ./requirements-pinned.txt --no-warn-script-location
RUN wine pip install --no-cache-dir -e . --no-dependencies --no-warn-script-location

# Build release
RUN wine pyinstaller \
    snaik/__main__.py \
    --clean \
    --noconfirm \
    --log-level=WARN \
    --windowed \
    --add-data "snaik/resources;snaik/resources" \
    --name=snaik \
    --distpath="/dist"

CMD ["/bin/bash"]
