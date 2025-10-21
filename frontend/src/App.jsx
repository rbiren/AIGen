import { useState } from 'react'
import './App.css'
import ImageUpload from './components/ImageUpload'
import ImageGallery from './components/ImageGallery'
import Header from './components/Header'

function App() {
  const [images, setImages] = useState([])
  const [processing, setProcessing] = useState(false)

  const handleImageUpload = async (files) => {
    setProcessing(true)

    try {
      const newImages = []

      for (const file of files) {
        const reader = new FileReader()

        const imageData = await new Promise((resolve) => {
          reader.onloadend = () => {
            resolve({
              id: Date.now() + Math.random(),
              name: file.name,
              url: reader.result,
              size: file.size,
              type: file.type,
              uploadedAt: new Date().toISOString()
            })
          }
          reader.readAsDataURL(file)
        })

        newImages.push(imageData)
      }

      setImages(prev => [...newImages, ...prev])
    } catch (error) {
      console.error('Error processing images:', error)
      alert('Failed to process images. Please try again.')
    } finally {
      setProcessing(false)
    }
  }

  const handleDeleteImage = (id) => {
    setImages(prev => prev.filter(img => img.id !== id))
  }

  const handleClearAll = () => {
    if (window.confirm('Are you sure you want to clear all images?')) {
      setImages([])
    }
  }

  return (
    <div className="app">
      <Header />

      <main className="main-content">
        <div className="container">
          <ImageUpload
            onUpload={handleImageUpload}
            processing={processing}
          />

          {images.length > 0 && (
            <div className="gallery-section">
              <div className="gallery-header">
                <h2>Your Images ({images.length})</h2>
                <button
                  className="btn-clear-all"
                  onClick={handleClearAll}
                >
                  Clear All
                </button>
              </div>

              <ImageGallery
                images={images}
                onDelete={handleDeleteImage}
              />
            </div>
          )}

          {images.length === 0 && !processing && (
            <div className="empty-state">
              <svg
                className="empty-icon"
                fill="none"
                stroke="currentColor"
                viewBox="0 0 24 24"
              >
                <path
                  strokeLinecap="round"
                  strokeLinejoin="round"
                  strokeWidth={2}
                  d="M4 16l4.586-4.586a2 2 0 012.828 0L16 16m-2-2l1.586-1.586a2 2 0 012.828 0L20 14m-6-6h.01M6 20h12a2 2 0 002-2V6a2 2 0 00-2-2H6a2 2 0 00-2 2v12a2 2 0 002 2z"
                />
              </svg>
              <p>No images yet. Upload some to get started!</p>
            </div>
          )}
        </div>
      </main>

      <footer className="footer">
        <p>Powered by AI | Built with React</p>
      </footer>
    </div>
  )
}

export default App
