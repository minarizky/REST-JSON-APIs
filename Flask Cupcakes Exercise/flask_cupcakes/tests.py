import unittest
from app import app, db, Cupcake

class CupcakeTestCase(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///test_cupcakes'
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_get_cupcakes(self):
        response = self.client.get('/api/cupcakes')
        self.assertEqual(response.status_code, 200)
        self.assertIn('cupcakes', response.json)

    def test_get_single_cupcake(self):
        cupcake = Cupcake(flavor='test', size='test', rating=5.0, image='test.jpg')
        db.session.add(cupcake)
        db.session.commit()

        response = self.client.get(f'/api/cupcakes/{cupcake.id}')
        self.assertEqual(response.status_code, 200)
        self.assertIn('cupcake', response.json)

    def test_create_cupcake(self):
        response = self.client.post('/api/cupcakes', json={
            'flavor': 'test',
            'size': 'test',
            'rating': 5.0,
            'image': 'test.jpg'
        })
        self.assertEqual(response.status_code, 201)
        self.assertIn('cupcake', response.json)

    def test_update_cupcake(self):
        cupcake = Cupcake(flavor='test', size='test', rating=5.0, image='test.jpg')
        db.session.add(cupcake)
        db.session.commit()

        response = self.client.patch(f'/api/cupcakes/{cupcake.id}', json={
            'flavor': 'updated',
            'size': 'updated',
            'rating': 4.0,
            'image': 'updated.jpg'
        })
        self.assertEqual(response.status_code, 200)
        self.assertIn('cupcake', response.json)
        self.assertEqual(response.json['cupcake']['flavor'], 'updated')

    def test_delete_cupcake(self):
        cupcake = Cupcake(flavor='test', size='test', rating=5.0, image='test.jpg')
        db.session.add(cupcake)
        db.session.commit()

        response = self.client.delete(f'/api/cupcakes/{cupcake.id}')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['message'], 'Deleted')

if __name__ == '__main__':
    unittest.main()
