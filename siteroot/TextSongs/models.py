from django.db.models import *

class Performers(Model):
    name = CharField(max_length=80)
    img = ImageField(upload_to='images/', null= True, blank=True)
    small_text = TextField(default=' ')
    large_text = TextField(default=' ')
    main_img = ImageField(upload_to='images/', null= True, blank=True)
    img_slider1 = ImageField(upload_to='images/', null= True, blank=True)
    img_slider2 = ImageField(upload_to='images/', null= True, blank=True)
    img_slider3 = ImageField(upload_to='images/', null= True, blank=True)
    created_at = DateTimeField('creation timestamp', auto_now_add=True)

    def __str__(self):
        return str(self.name)


class Albums(Model):
    title = CharField(max_length=80)
    year_of_created = IntegerField()
    author = ForeignKey(Performers, on_delete=CASCADE)
    img = ImageField(upload_to='images/', null=True, blank=True)
    created_at = DateTimeField('creation timestamp', auto_now_add=True)

    def get_title(self):
        b = self.title.split()
        b = ''.join(b)
        return b

    def get_songs(self):
        songs = Songs.objects.filter(album=self.id)
        b = {'songs': songs}
        return b


    def __str__(self):
        return str(self.title)

class Songs(Model):
    title = CharField(max_length=80)
    title_en = CharField(max_length=80, default='0000000')
    author = ForeignKey(Performers, on_delete=CASCADE)
    album = ForeignKey(Albums, on_delete=RESTRICT)
    text = TextField()
    created_at = DateTimeField('creation timestamp', auto_now_add=True)

    def get_text(self):
        text = self.text
        return text

    def __str__(self):
        return str(self.title)

class OrderText(Model):
    artist_name = CharField(max_length=80)
    album_name = CharField(max_length=80)
    song_name = CharField(max_length=80)
    info = TextField(null=True, blank=True)
    created_at = DateTimeField('creation timestamp', auto_now_add=True)

    def __str__(self):
        return str(self.artist_name + ' ' + self.song_name )