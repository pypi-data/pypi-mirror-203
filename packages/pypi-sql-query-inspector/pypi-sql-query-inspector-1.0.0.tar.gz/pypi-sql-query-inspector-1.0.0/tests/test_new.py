import pytest
import sys
from django.urls import reverse

pytestmark = pytest.mark.django_db


# client, settings, capsys - are all built-in pytest/pytest-django fixtures!
@pytest.mark.urls('demo_app.urls')
def test_demo(client, settings, capsys):
    settings.DEBUG = True
    url = reverse('test_endpoint')
    response = client.get(url)

    captured = capsys.readouterr()
    sys.stdout.write(captured.out)

    assert "1 Total queries" in captured.out
    assert response.status_code == 200
