
import media
import fresh_tomatoes

"""Creates 1st instance"""
jurassic_park = media.Movie(
                "Jurassic Park",
                "A disastrous attempt to create a theme park of cloned dinosaurs",
                "https://ak-hdl.buzzfed.com/static/2014-08/12/12/enhanced/webdr10/enhanced-14020-1407861668-13.jpg",
                "https://www.youtube.com/watch?v=lc0UehYemQA")

"""Creates 2nd instance"""
napoleon_dynamite = media.Movie(
                "Napoleon Dynamite",
                "A socially awkward 16-year-old boy from Preston, Idaho.",
                "http://0f1b361a5a35d46c59b38689aef7623c.fslcdn.net/media/spotlight/page/poster-650849c3-e0a4-4c85-beaa-3700ba512613.jpg",
                "https://www.youtube.com/watch?v=ZHDi_AnqwN4")

"""Creates 3rd instance"""
forgetting_sarah_marshall = media.Movie(
                "Forgetting Sarah Marshall",
                "Composer Peter Bretter is in a failing relationship.",
                "http://ecx.images-amazon.com/images/I/61WsZOy-ZrL.jpg",
                "https://www.youtube.com/watch?v=PyVEHIO6jZ0")

"""Creates array of movies"""
movies = [jurassic_park, napoleon_dynamite,forgetting_sarah_marshall]
#print (media.Movie.__doc__)
"""imvokes fresh_tomatoes and run open_movies_page() function"""
fresh_tomatoes.open_movies_page(movies) 
