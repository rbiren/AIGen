import { useRef, useState } from 'react'
import './ImageUpload.css'

function ImageUpload({ onUpload, processing }) {
  const fileInputRef = useRef(null)
  const [dragActive, setDragActive] = useState(false)

  const handleDrag = (e) => {
    e.preventDefault()
    e.stopPropagation()

    if (e.type === 'dragenter' || e.type === 'dragover') {
      setDragActive(true)
    } else if (e.type === 'dragleave') {
      setDragActive(false)
    }
  }

  const handleDrop = (e) => {
    e.preventDefault()
    e.stopPropagation()
    setDragActive(false)

    if (e.dataTransfer.files && e.dataTransfer.files.length > 0) {
      handleFiles(e.dataTransfer.files)
    }
  }

  const handleChange = (e) => {
    e.preventDefault()
    if (e.target.files && e.target.files.length > 0) {
      handleFiles(e.target.files)
    }
  }

  const handleFiles = (files) => {
    const imageFiles = Array.from(files).filter(file =>
      file.type.startsWith('image/')
    )

    if (imageFiles.length === 0) {
      alert('Please select valid image files')
      return
    }

    if (imageFiles.length !== files.length) {
      alert('Some files were skipped because they are not images')
    }

    onUpload(imageFiles)
  }

  const handleClick = () => {
    fileInputRef.current?.click()
  }

  return (
    <div className="upload-section">
      <div
        className={`upload-area ${dragActive ? 'drag-active' : ''} ${processing ? 'processing' : ''}`}
        onDragEnter={handleDrag}
        onDragLeave={handleDrag}
        onDragOver={handleDrag}
        onDrop={handleDrop}
        onClick={handleClick}
      >
        <input
          ref={fileInputRef}
          type="file"
          multiple
          accept="image/*"
          onChange={handleChange}
          style={{ display: 'none' }}
        />

        {processing ? (
          <div className="processing-state">
            <div className="spinner"></div>
            <p>Processing images...</p>
          </div>
        ) : (
          <>
            <svg
              className="upload-icon"
              fill="none"
              stroke="currentColor"
              viewBox="0 0 24 24"
            >
              <path
                strokeLinecap="round"
                strokeLinejoin="round"
                strokeWidth={2}
                d="M7 16a4 4 0 01-.88-7.903A5 5 0 1115.9 6L16 6a5 5 0 011 9.9M15 13l-3-3m0 0l-3 3m3-3v12"
              />
            </svg>

            <h3>Upload Your Images</h3>
            <p className="upload-hint">
              Drag and drop your images here, or click to browse
            </p>
            <p className="upload-note">
              Supports: JPG, PNG, GIF, WebP
            </p>

            <button className="btn-upload" type="button">
              Choose Files
            </button>
          </>
        )}
      </div>
    </div>
  )
}

export default ImageUpload
