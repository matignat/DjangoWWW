# Create your tests here.
from django.test import TestCase

class PagesTests(TestCase):

    def test_home_status(self):
        response = self.client.get("/")
        assert response.status_code == 200

    def test_about_uses_correct_template(self):
        response = self.client.get("/about/")
        # TODO: assert "pages/about.html" was used (hint: assertTemplateUsed)
        self.assertTemplateUsed(response, "pages/about.html")

    def test_about_has_four_skills(self):
        response = self.client.get("/about/")
        # TODO: assert len(response.context["skills"]) == 4
        self.assertEqual(len(response.context["skills"]), 4)

    def test_greet_contains_name(self):
        response = self.client.get("/greet/Alice/")
        # TODO: assert b"Alice" in response.content
        assert b"Alice" in response.content

    def test_projects_search_filters(self):
        response = self.client.get("/projects/?q=python")
        # TODO: assert every project in response.context["project_list"]
        #       has lang == "Python" or name containing "python" (case-insensitive)
        for project in response.context["project_list"]:
            assert project["lang"] == "Python" or "python" in project["name"].lower()