import data
import hw2
import unittest


# Write your test cases for each part below.

class TestCases(unittest.TestCase):
    # Part 1
    def test_create_rectangle(self):
        points1=data.Point(1,2)
        points2=data.Point(4,6)
        result=hw2.create_rectangle(points1,points2)
        expected=data.Rectangle(data.Point(1,6),data.Point(4,2))
        self.assertEqual(result,expected)
    def test_create_rectangle2(self):
        points1=data.Point(3,8)
        points2=data.Point(7,8)
        result=hw2.create_rectangle(points1,points2)
        expected=data.Rectangle(data.Point(3,8),data.Point(7,8))
        self.assertEqual(result,expected)

    # Part 2
    def test_shorter_duration_than(self):
        time1=data.Duration(6,30)
        time2=data.Duration(5,40)
        result=hw2.shorter_duration_than(time1,time2)
        expected=False
        self.assertEqual(result, expected)
    def test_shorter_duration_than2(self):
        time1=data.Duration(4,30)
        time2=data.Duration(5,35)
        result=hw2.shorter_duration_than(time1,time2)
        expected=True
        self.assertEqual(result, expected)

    # Part 3
    def test_song_shorter_than(self):
        song_list=[data.Song("Artist1","title1",data.Duration(5,55)),
                   data.Song("Artist2","title2",data.Duration(4,35)),
                   data.Song("Artist3","title3",data.Duration(3,40))]
        result=hw2.song_shorter_than(song_list,data.Duration(5,0))
        expected=[data.Song("Artist2","title2",data.Duration(4,35)),
                  data.Song("Artist3","title3",data.Duration(3,40))]
        self.assertEqual(result, expected)
    def test_song_shorter_than2(self):
        song_list=[data.Song("Artist1","title1",data.Duration(3,20)),
                   data.Song("Artist2","title2",data.Duration(6,19)),
                   data.Song("Artist3","title3",data.Duration(7,8))]
        result=hw2.song_shorter_than(song_list,data.Duration(4,0))
        expected=[data.Song("Artist1","title1",data.Duration(3,20))]
        self.assertEqual(result, expected)
    # Part 4
    def test_running_time(self):
        song_list=[data.Song("Artist1","title1",data.Duration(5,55)),
                   data.Song("Artist2","title2",data.Duration(4,35)),
                   data.Song("Artist3","title3",data.Duration(3,40))]
        result=hw2.running_time(song_list,[0,1,2])
        expected=data.Duration(14,10)
        self.assertEqual(result, expected)
    def test_running_time2(self):
        song_list=[data.Song("Artist1","title1",data.Duration(5,55)),
                   data.Song("Artist2","title2",data.Duration(4,35)),
                   data.Song("Artist3","title3",data.Duration(3,40))]
        result=hw2.running_time(song_list,[0,1,2,0,2])
        expected=data.Duration(23,45)
        self.assertEqual(result, expected)

    # Part 5
    def test_validate_route(self):
        city_links = [['san luis obispo', 'santa margarita'],
                      ['san luis obispo', 'pismo beach'],
                      ['atascadero', 'santa margarita'],
                      ['atascadero', 'creston']]
        result=hw2.validate_route(city_links,['san luis obispo','santa margarita', 'atascadero'])
        expected=True
        self.assertEqual(result, expected)
    def test_validate_route2(self):
        city_links = [['Los Angeles', 'Santa Monica'],
                      ['Los Angeles', 'Culver City'],
                      ['Westwood', 'Culver City'],
                      ['Santa Monica','Culver City']]
        result=hw2.validate_route(city_links,['Los Angeles', 'Westwood'])
        expected=False
        self.assertEqual(result, expected)
    # Part 6
    def test_longest_repetition(self):
        num_list=[1,1,2,2,2,2,2,1,1,1,1,3]
        result=hw2.longest_repetition(num_list)
        expected=2
        self.assertEqual(result, expected)
    def test_longest_repetition2(self):
        num_list=[4,5,5,6,6,6,6,3,3,3,3,2,2,6,8,8,8]
        result=hw2.longest_repetition(num_list)
        expected=3
        self.assertEqual(result, expected)




if __name__ == '__main__':
    unittest.main()
