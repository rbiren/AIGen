import './ImageGallery.css'

function ImageGallery({ images, onDelete }) {
  const formatFileSize = (bytes) => {
    if (bytes === 0) return '0 Bytes'
    const k = 1024
    const sizes = ['Bytes', 'KB', 'MB', 'GB']
    const i = Math.floor(Math.log(bytes) / Math.log(k))
    return Math.round(bytes / Math.pow(k, i) * 100) / 100 + ' ' + sizes[i]
  }

  return (
    <div className="image-gallery">
      {images.map((image) => (
        <div key={image.id} className="image-card">
          <div className="image-wrapper">
            <img src={image.url} alt={image.name} />
            <div className="image-overlay">
              <button
                className="btn-delete"
                onClick={() => onDelete(image.id)}
                title="Delete image"
              >
                <svg
                  fill="none"
                  stroke="currentColor"
                  viewBox="0 0 24 24"
                  width="20"
                  height="20"
                >
                  <path
                    strokeLinecap="round"
                    strokeLinejoin="round"
                    strokeWidth={2}
                    d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16"
                  />
                </svg>
              </button>
            </div>
          </div>

          <div className="image-info">
            <p className="image-name" title={image.name}>
              {image.name}
            </p>
            <p className="image-size">
              {formatFileSize(image.size)}
            </p>
          </div>
        </div>
      ))}
    </div>
  )
}

export default ImageGallery
