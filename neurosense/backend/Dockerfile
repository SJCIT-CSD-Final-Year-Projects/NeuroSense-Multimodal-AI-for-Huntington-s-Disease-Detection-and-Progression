# NeuroSense AI API — Dockerfile for Railway & Cloud Deployment
FROM python:3.10-slim

# System dependencies for OpenCV, scientific computing, and medical imaging
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libgl1 \
    libglib2.0-0 \
    git \
    && rm -rf /var/lib/apt/lists/*

# Hugging Face Spaces runs as user with UID 1000
RUN useradd -m -u 1000 user

# Set working directory and ownership
WORKDIR /app
RUN chown -R user:user /app

# Switch to non-root user
USER user
ENV HOME=/home/user \
    PATH=/home/user/.local/bin:$PATH \
    PYTHONUNBUFFERED=1 \
    PYTHONPATH=/app

# Install lightweight CPU-only PyTorch first (drastically reduces image size & build time)
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir torch torchvision --index-url https://download.pytorch.org/whl/cpu

# Copy requirements and install
COPY --chown=user:user neurosense/backend/requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt

# Copy application source code
COPY --chown=user:user . /app

# Ensure directories for outputs and uploads exist with write permissions
RUN mkdir -p /app/neurosense/backend/outputs/heatmaps /app/neurosense/backend/uploads /app/neurosense/backend/checkpoints

# Railway assigns $PORT dynamically; default to 8000 for local Docker builds
EXPOSE 8000

# Launch FastAPI with uvicorn — uses $PORT from Railway, falls back to 8000
CMD ["sh", "-c", "uvicorn neurosense.backend.api.main:app --host 0.0.0.0 --port ${PORT:-8000}"]
