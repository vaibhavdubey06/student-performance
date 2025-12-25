"""
Tests for the prediction pipeline.
"""

import pytest
import pandas as pd
import numpy as np
import os
import sys

# Add project root to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.pipeline.predict_pipeline import CustomData, PredictPipeline


class TestCustomData:
    """Tests for the CustomData class."""

    def test_custom_data_creation(self):
        """Test that CustomData can be instantiated with valid inputs."""
        data = CustomData(
            gender="female",
            race_ethnicity="group B",
            parental_level_of_education="bachelor's degree",
            lunch="standard",
            test_preparation_course="completed",
            reading_score=72,
            writing_score=74,
        )

        assert data.gender == "female"
        assert data.race_ethnicity == "group B"
        assert data.reading_score == 72
        assert data.writing_score == 74

    def test_get_data_as_dataframe(self):
        """Test that CustomData converts to DataFrame correctly."""
        data = CustomData(
            gender="male",
            race_ethnicity="group C",
            parental_level_of_education="some college",
            lunch="free/reduced",
            test_preparation_course="none",
            reading_score=65,
            writing_score=60,
        )

        df = data.get_data_as_data_frame()

        assert isinstance(df, pd.DataFrame)
        assert len(df) == 1
        assert "gender" in df.columns
        assert "reading_score" in df.columns
        assert "writing_score" in df.columns
        assert df["gender"].iloc[0] == "male"
        assert df["reading_score"].iloc[0] == 65

    def test_dataframe_has_correct_columns(self):
        """Test that the DataFrame has all required columns."""
        data = CustomData(
            gender="female",
            race_ethnicity="group A",
            parental_level_of_education="high school",
            lunch="standard",
            test_preparation_course="completed",
            reading_score=80,
            writing_score=85,
        )

        df = data.get_data_as_data_frame()

        expected_columns = [
            "gender",
            "race_ethnicity",
            "parental_level_of_education",
            "lunch",
            "test_preparation_course",
            "reading_score",
            "writing_score",
        ]

        for col in expected_columns:
            assert col in df.columns, f"Missing column: {col}"


class TestPredictPipeline:
    """Tests for the PredictPipeline class."""

    @pytest.fixture
    def sample_data(self):
        """Create sample input data for predictions."""
        return CustomData(
            gender="female",
            race_ethnicity="group B",
            parental_level_of_education="bachelor's degree",
            lunch="standard",
            test_preparation_course="completed",
            reading_score=72,
            writing_score=74,
        )

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
    def test_prediction_returns_array(self, sample_data):
        """Test that prediction returns a numpy array."""
        pipeline = PredictPipeline()
        df = sample_data.get_data_as_data_frame()
        result = pipeline.predict(df)

        assert isinstance(result, np.ndarray)
        assert len(result) == 1

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
    def test_prediction_in_valid_range(self, sample_data):
        """Test that prediction is in valid score range (0-100)."""
        pipeline = PredictPipeline()
        df = sample_data.get_data_as_data_frame()
        result = pipeline.predict(df)

        # Math scores should be between 0 and 100
        assert 0 <= result[0] <= 100, f"Prediction {result[0]} out of range"

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
    def test_prediction_consistency(self, sample_data):
        """Test that same input gives same output (deterministic)."""
        pipeline = PredictPipeline()
        df = sample_data.get_data_as_data_frame()

        result1 = pipeline.predict(df)
        result2 = pipeline.predict(df)

        assert result1[0] == result2[0], "Predictions should be deterministic"


class TestDataValidation:
    """Tests for input data validation."""

    def test_valid_gender_values(self):
        """Test that valid gender values work."""
        for gender in ["male", "female"]:
            data = CustomData(
                gender=gender,
                race_ethnicity="group A",
                parental_level_of_education="high school",
                lunch="standard",
                test_preparation_course="none",
                reading_score=50,
                writing_score=50,
            )
            df = data.get_data_as_data_frame()
            assert df["gender"].iloc[0] == gender

    def test_valid_lunch_values(self):
        """Test that valid lunch values work."""
        for lunch in ["standard", "free/reduced"]:
            data = CustomData(
                gender="male",
                race_ethnicity="group A",
                parental_level_of_education="high school",
                lunch=lunch,
                test_preparation_course="none",
                reading_score=50,
                writing_score=50,
            )
            df = data.get_data_as_data_frame()
            assert df["lunch"].iloc[0] == lunch

    def test_score_boundary_values(self):
        """Test boundary values for scores."""
        # Test minimum valid scores
        data_min = CustomData(
            gender="male",
            race_ethnicity="group A",
            parental_level_of_education="high school",
            lunch="standard",
            test_preparation_course="none",
            reading_score=0,
            writing_score=0,
        )
        df_min = data_min.get_data_as_data_frame()
        assert df_min["reading_score"].iloc[0] == 0

        # Test maximum valid scores
        data_max = CustomData(
            gender="male",
            race_ethnicity="group A",
            parental_level_of_education="high school",
            lunch="standard",
            test_preparation_course="none",
            reading_score=100,
            writing_score=100,
        )
        df_max = data_max.get_data_as_data_frame()
        assert df_max["reading_score"].iloc[0] == 100
