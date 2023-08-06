import os
import tempfile
import time
from unittest import TestCase

import matplotlib.pyplot as plt

from gig import Ent, EntType

TEST_ENT = Ent.from_id('LK-11')
DIR_TMP = tempfile.gettempdir()


class TestEntGeoMixin(TestCase):
    def test_url_remote_geo_data_path(self):
        print(TEST_ENT.url_remote_geo_data_path)

        self.assertEqual(
            TEST_ENT.url_remote_geo_data_path,
            '/'.join(
                [
                    'https://raw.githubusercontent.com',
                    'nuuuwan',
                    'gig-data',
                    'master',
                    'geo',
                    'district',
                    'LK-11.json',
                ]
            ),
        )

    def test_raw_geo(self):
        raw_geo = TEST_ENT.get_raw_geo()
        self.assertEqual(len(raw_geo), 2)
        self.assertEqual(len(raw_geo[0]), 23)
        self.assertEqual(len(raw_geo[0][0]), 2)
        self.assertAlmostEqual(raw_geo[0][0][0], 79.84781552236845)
        self.assertAlmostEqual(raw_geo[0][0][1], 6.956820193543937)

    def test_geo(self):
        for id in ['LK-1', 'LK-11', 'LK-1127', 'LK-1127025']:
            ent = Ent.from_id(id)
            geo = ent.geo()
            geo.plot()
            png_file_name = f'gig.TestEntGeoMixin.{id}.png'
            test_png_file_path = os.path.join(DIR_TMP, png_file_name)
            plt.savefig(test_png_file_path)
            plt.close()

            control_png_file_path = os.path.join('tests', png_file_name)
            self.assertEqual(
                os.path.getsize(test_png_file_path),
                os.path.getsize(control_png_file_path),
            )

    def test_example_1_westernish_province(self):
        _, ax = plt.subplots(figsize=(16, 9))

        for id, color in [
            ['LK-11', 'green'],
            ['LK-12', 'blue'],
            ['LK-62', 'darkgreen'],
        ]:
            ent = Ent.from_id(id)
            geo = ent.geo()
            geo.plot(ax=ax, color=color)

        png_file_name = 'gig.TestEntGeoMixin.example1.png'
        test_png_file_path = os.path.join(DIR_TMP, png_file_name)
        plt.savefig(test_png_file_path)
        plt.close()

        control_png_file_path = os.path.join('tests', png_file_name)
        self.assertEqual(
            os.path.getsize(test_png_file_path),
            os.path.getsize(control_png_file_path),
        )

    def test_example_2_lgs(self):
        _, ax = plt.subplots(figsize=(16, 9))
        lg_ents = Ent.list_from_type(EntType.LG)

        # dummy load run
        N_ENTS = 20
        for ent in lg_ents[:N_ENTS]:
            ent.geo()

        t0 = time.time()
        for ent in lg_ents[:N_ENTS]:
            geo = ent.geo()
            geo.plot(ax=ax, color='#0c0')
        dt = time.time() - t0
        mean_t = dt / N_ENTS

        png_file_name = 'gig.TestEntGeoMixin.example2.png'
        test_png_file_path = os.path.join(DIR_TMP, png_file_name)
        plt.savefig(test_png_file_path)
        plt.close()
        self.assertLess(mean_t, 0.1)
