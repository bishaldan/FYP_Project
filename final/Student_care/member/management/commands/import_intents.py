import json
from django.core.management.base import BaseCommand
from member.models import Intent


class Command(BaseCommand):
    help = 'Imports intents from a JSON file into the database'

    def handle(self, *args, **kwargs):
        # Update this with the correct file path
        json_file_path = 'C:\\Users\\Mr Bishal\\OneDrive\\FYP_project\\Chatbot\\final\\Student_care\\member\\intents.json'
        with open(json_file_path, 'r') as file:
            intents_data = json.load(file)
            intents = intents_data.get('intents', [])
            for intent_data in intents:
                patterns = intent_data.get('patterns', [])
                if patterns:  # Ensure patterns is not empty
                    intent = Intent.objects.create(
                        tag=intent_data.get('tag', ''),
                        patterns=patterns,  # Assign patterns here
                        responses=intent_data.get('responses', [])
                    )
                    self.stdout.write(self.style.SUCCESS(
                        f'Imported intent: {intent.tag}'))
                else:
                    self.stdout.write(self.style.WARNING(
                        'Skipping intent with empty patterns'))
