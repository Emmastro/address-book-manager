import logging

from django.core.management.base import BaseCommand

import pandas as pd

from faker import Faker

from contact.models import Contact

logging.basicConfig(level=logging.INFO)


class Command(BaseCommand):

    def add_arguments(self, parser):

        parser.add_argument('--file', type=str)

    def handle(self, *args, **options):

        if hasattr(options, 'file'):  # import from the file of a file is given on the command line
            df = pd.read_csv(options['file'])
        else:
            # creates a dataset using faker
            faker = Faker()
            data = []
            for l in range(50):
                data.append(
                    (
                        faker.first_name(),
                        faker.last_name(),
                        faker.phone_number(),
                        faker.address(),
                        faker.email()
                    )
                )

            df = pd.DataFrame(
                columns=['first_name', 'last_name', 'phone_number', 'address', 'email'], data=data)

        # TODO: validate data before saving
        for index, row in df.iterrows():
            contact = Contact(**row.to_dict())
            contact.save()
            logging.info(
                f'{contact.first_name} {contact.last_name} added to database')

        logging.info(f'{len(df)} contacts added to database')
