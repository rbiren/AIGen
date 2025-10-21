# AIGen - AI-Powered Photo Processing

A modern web application for AI-powered photo processing and management, built with React and Azure Functions.

## Features

- Modern, responsive React-based user interface
- Drag-and-drop image upload
- Real-time image preview and gallery
- Azure Functions serverless backend
- Cloud-ready deployment configuration

## Project Structure

```
AIGen/
├── frontend/                  # React frontend application
│   ├── src/
│   │   ├── components/       # React components
│   │   │   ├── Header.jsx
│   │   │   ├── ImageUpload.jsx
│   │   │   └── ImageGallery.jsx
│   │   ├── App.jsx           # Main application component
│   │   ├── App.css
│   │   ├── main.jsx          # React entry point
│   │   └── index.css
│   ├── index.html
│   ├── package.json
│   └── vite.config.js        # Vite build configuration
├── function_app.py           # Azure Functions backend
├── host.json                 # Azure Functions host configuration
├── requirements.txt          # Python dependencies
└── .github/workflows/        # CI/CD pipeline
    └── main_aiphotos.yml
```

## Tech Stack

### Frontend
- **React 18** - Modern UI library
- **Vite** - Fast build tool and dev server
- **CSS3** - Styling with modern features

### Backend
- **Python 3.11** - Backend runtime
- **Azure Functions** - Serverless compute platform
- **Pillow** - Image processing library

## Getting Started

### Prerequisites

- Node.js 18+ and npm
- Python 3.11+
- Azure Functions Core Tools (for local development)

### Frontend Development

1. Navigate to the frontend directory:
```bash
cd frontend
```

2. Install dependencies:
```bash
npm install
```

3. Start the development server:
```bash
npm run dev
```

The frontend will be available at `http://localhost:3000`

4. Build for production:
```bash
npm run build
```

### Backend Development

1. Create a virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Copy the example settings file:
```bash
cp local.settings.json.example local.settings.json
```

4. Start the Azure Functions locally:
```bash
func start
```

The API will be available at `http://localhost:7071`

## API Endpoints

### Health Check
```
GET /api/health
```
Returns the health status of the API.

### Process Image
```
POST /api/process
```
Upload and process an image with AI.

**Request:** Multipart form data with image file

**Response:**
```json
{
  "success": true,
  "message": "Image processed successfully",
  "filename": "example.jpg",
  "timestamp": "2025-10-21T12:00:00",
  "processing": {
    "status": "completed",
    "ai_analysis": "..."
  }
}
```

### Get Images
```
GET /api/images
```
Retrieve a list of processed images.

## Deployment

The application is configured for automatic deployment to Azure using GitHub Actions.

### Azure Deployment

The project includes a GitHub Actions workflow that automatically deploys to Azure when code is pushed to the main branch.

**Deployment targets:**
- Frontend: Azure Static Web Apps (or your preferred hosting)
- Backend: Azure Functions App (`aiphotos`)

### Environment Variables

For local development, create a `local.settings.json` file based on `local.settings.json.example`.

## Development Workflow

1. Create a feature branch from main
2. Make your changes
3. Test locally (frontend + backend)
4. Commit and push to your branch
5. Create a pull request
6. After merge, automatic deployment will trigger

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a pull request

## License

This project is private and proprietary.

## Support

For issues or questions, please create an issue in the GitHub repository.