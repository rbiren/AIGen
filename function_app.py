import azure.functions as func
import json
import logging
from datetime import datetime

app = func.FunctionApp()

@app.route(route="health", methods=["GET"], auth_level=func.AuthLevel.ANONYMOUS)
def health_check(req: func.HttpRequest) -> func.HttpResponse:
    """Health check endpoint"""
    logging.info('Health check endpoint called')

    return func.HttpResponse(
        json.dumps({
            "status": "healthy",
            "timestamp": datetime.utcnow().isoformat(),
            "service": "AIGen API"
        }),
        mimetype="application/json",
        status_code=200
    )


@app.route(route="process", methods=["POST"], auth_level=func.AuthLevel.ANONYMOUS)
def process_image(req: func.HttpRequest) -> func.HttpResponse:
    """Process uploaded image with AI"""
    logging.info('Process image endpoint called')

    try:
        # Get the uploaded file
        files = req.files

        if not files:
            return func.HttpResponse(
                json.dumps({"error": "No image file provided"}),
                mimetype="application/json",
                status_code=400
            )

        # Get the first file
        image_file = files.get('image')

        if not image_file:
            return func.HttpResponse(
                json.dumps({"error": "No image file in request"}),
                mimetype="application/json",
                status_code=400
            )

        # Here you would add your AI processing logic
        # For now, we'll return a success response

        response_data = {
            "success": True,
            "message": "Image processed successfully",
            "filename": image_file.filename,
            "timestamp": datetime.utcnow().isoformat(),
            "processing": {
                "status": "completed",
                "ai_analysis": "Placeholder - Add your AI model here"
            }
        }

        return func.HttpResponse(
            json.dumps(response_data),
            mimetype="application/json",
            status_code=200
        )

    except Exception as e:
        logging.error(f"Error processing image: {str(e)}")
        return func.HttpResponse(
            json.dumps({
                "error": "Failed to process image",
                "details": str(e)
            }),
            mimetype="application/json",
            status_code=500
        )


@app.route(route="images", methods=["GET"], auth_level=func.AuthLevel.ANONYMOUS)
def get_images(req: func.HttpRequest) -> func.HttpResponse:
    """Get list of processed images"""
    logging.info('Get images endpoint called')

    # This is a placeholder. In production, you would fetch from a database
    sample_images = [
        {
            "id": "1",
            "name": "sample1.jpg",
            "processed_at": datetime.utcnow().isoformat(),
            "status": "completed"
        },
        {
            "id": "2",
            "name": "sample2.jpg",
            "processed_at": datetime.utcnow().isoformat(),
            "status": "completed"
        }
    ]

    return func.HttpResponse(
        json.dumps({
            "images": sample_images,
            "count": len(sample_images)
        }),
        mimetype="application/json",
        status_code=200
    )
