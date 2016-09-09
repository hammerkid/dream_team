import unittest
import sim

class TestSyncerObject (unittest.TestCase):
    def test(self):
        s = sim.Syncer()
        self.assertEquals(s.name, 'syncer' or 'syncer2')

if __name__ == '__main__':
    unittest.main()