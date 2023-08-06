from classification_model.config.core import config
from classification_model.processing.cabin_encoder import CabinEncoder


def test_cabin_encoder(sample_input_data):
    # Given
    transformer = CabinEncoder(
        variables=config.model_config.cabin_vars
    )
    assert sample_input_data["Cabin"].iat[12] == 'B45'

    # When
    subject = transformer.fit_transform(sample_input_data)

    # Then
    assert subject["Cabin_Level"].iat[12] == 'Upper'
