"""
Tests for the Flask application.
"""

import pytest
import sys
import os

# Add project root to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app import app


@pytest.fixture
def client():
    """Create a test client for the Flask app."""
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


class TestHealthEndpoints:
    """Tests for basic health/status endpoints."""

    def test_home_page_loads(self, client):
        """Test that the home page loads successfully."""
        response = client.get("/")
        assert response.status_code == 200

    def test_predict_page_get(self, client):
        """Test that the prediction page loads with GET request."""
        response = client.get("/predictdata")
        assert response.status_code == 200


class TestPredictionEndpoint:
    """Tests for the prediction endpoint."""

    @pytest.mark.skipif(
        not os.path.exists(
            os.path.join(
                os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                "artifacts",
                "model.pkl",
            )
        ),
        reason="Model artifacts not found",
    )
    def test_prediction_post_valid_data(self, client):
        """Test prediction with valid form data."""
        response = client.post(
            "/predictdata",
            data={
                "gender": "female",
                "ethnicity": "group B",
                "parental_level_of_education": "bachelor's degree",
                "lunch": "standard",
                "test_preparation_course": "completed",
                "reading_score": "72",
                "writing_score": "74",
            },
        )
        assert response.status_code == 200
        # Check that the response contains a prediction result
        assert b"result-score" in response.data or b"Predicted" in response.data

    @pytest.mark.skipif(
        not os.path.exists(
            os.path.join(
                os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                "artifacts",
                "model.pkl",
            )
        ),
        reason="Model artifacts not found",
    )
    def test_prediction_different_inputs(self, client):
        """Test prediction with various valid inputs."""
        test_cases = [
            {
                "gender": "male",
                "ethnicity": "group A",
                "parental_level_of_education": "high school",
                "lunch": "free/reduced",
                "test_preparation_course": "none",
                "reading_score": "50",
                "writing_score": "45",
            },
            {
                "gender": "female",
                "ethnicity": "group E",
                "parental_level_of_education": "master's degree",
                "lunch": "standard",
                "test_preparation_course": "completed",
                "reading_score": "95",
                "writing_score": "98",
            },
        ]

        for data in test_cases:
            response = client.post("/predictdata", data=data)
            assert response.status_code == 200


class TestErrorHandling:
    """Tests for error handling."""

    def test_invalid_route_returns_404(self, client):
        """Test that invalid routes return 404."""
        response = client.get("/nonexistent")
        assert response.status_code == 404

    def test_invalid_method(self, client):
        """Test that invalid HTTP methods are handled."""
        response = client.put("/predictdata")
        assert response.status_code == 405  # Method Not Allowed
