import streamlit as st
import pandas as pd
import altair as alt

movies = pd.read_csv('data/movies.csv')

ratings = pd.read_csv('data/ratings.csv')

tags = pd.read_csv('data/tags.csv')

# Data visualization

movies["year"] = movies['title'].str.extract(r"\((\d{4})\)$")
st.subheader(":red[Number of movies per year]", divider="red")
movies_per_year = movies['year'].value_counts().sort_index()
st.bar_chart(movies_per_year, color="#AAA")
st.markdown("""
The 1970s : A decade of change, of revolution, and of unprecedented creativity in cinema. The silver screen was about to be transformed, and the seeds of this metamorphosis were sown in the fertile soil of a world in flux. 
Let's pull back the curtain and explore the extraordinary confluence of factors that led to a boom in film production during this unforgettable era.

**Technological Advancements**: Imagine a filmmaker in the 1960s, burdened by heavy, cumbersome equipment. Now, picture that same filmmaker a decade later, liberated by the technological advancements that swept through the 1970s. Lighter, more portable cameras, enhanced
film stocks, and advanced sound recording equipment—these innovations made filmmaking more accessible and affordable than ever before. The camera, once a lumbering beast, became a nimble tool, ready to capture life in all its raw, unscripted beauty.

**The New Hollywood Era**: As the studio system, the so-called 'Big Five' that had ruled Hollywood since the 1930s, began to crumble, a new generation of filmmakers emerged from the ashes. These rebels, these visionaries, were the architects of what came to be known as the
'New Hollywood' or the 'American New Wave.' They brought fresh ideas, unconventional approaches, and a fierce determination to tell stories that mattered. The old guard was fading, and in its place rose a creative force that would redefine cinema.

**Social and Cultural Changes**: The 1970s was a time of seismic social and cultural shifts. The Vietnam War raged on, civil rights battles were fought, women's liberation movements gained momentum, and the counterculture movement challenged the status quo. These tumultuous
times provided a wealth of material for filmmakers, who began to reflect the changing societal landscape with unflinching honesty. Movies became mirrors, held up to a world in transition, capturing the zeitgeist (spirit or mood of a particular time period) in all its complexity.

**The Rise of Independent Cinema**: With the decline of the studio system, independent cinema began to flourish. Filmmakers like Martin Scorsese, Francis Ford Coppola, and Steven Spielberg emerged as the new storytellers, crafting films that were not only critically
acclaimed but also commercially successful. These independent voices brought a fresh perspective, a raw energy, and a willingness to take risks that resonated with audiences hungry for something new.

**Introduction of the MPAA Rating System**: In 1968, the Motion Picture Association of America introduced its rating system, allowing for more explicit content in films. This newfound freedom led to an explosion of creativity, as filmmakers pushed the boundaries of what
could be shown on screen. Movies aimed at adult audiences flourished, tackling mature themes and exploring the human condition in all its complexity.

**Economic Factors**: The 1970s also saw an increase in disposable income for many people. With more money in their pockets, audiences flocked to movie theaters, creating a higher demand for films. The cinema became not just a place of entertainment but a cultural hub, a
gathering place where people could escape, dream, and engage with the stories of their time.

**Global Influences**: The influence of international cinema, particularly from Europe and Asia, also played a significant role in the increase in film production. American filmmakers were inspired by the creative and artistic innovations of foreign films, drawing on these
influences to craft their own unique visions. The world of cinema was becoming more interconnected, more global, and the result was a rich tapestry of stories that transcended borders and cultures.

These factors collectively contributed to a boom in film production during the 1970s, a decade that would forever change the landscape of cinema. It was a time of innovation, of rebellion, and of unparalleled creativity—a golden age that continues to inspire
and influence filmmakers today.

And so, the 1970s became a decade of cinematic revolution, a testament to the power of storytelling and the enduring magic of the silver screen.
""")

st.divider()

st.subheader(":red[Number of movies per genre]", divider="red")
genres = movies['genres'].str.split('|', expand=True).stack(
).value_counts().sort_values(ascending=False)

# Genres chart

genres = genres.reset_index()
genres.columns = ['genre', 'count']
genres_chart = alt.Chart(genres).mark_bar().encode(
    x='count',
    y=alt.Y('genre', sort='-x'),
    color='genre'
)
st.altair_chart(genres_chart, use_container_width=True)

st.write(""" 

As we delve into the annals of cinema, one genre stands out as the undisputed champion of audience engagement and emotional resonance: **Drama**. With an astounding 4361 movies to its credit, the drama genre has carved a deep and enduring niche in the hearts of film lovers worldwide.

A movie drama is more than just a feature film; it is a journey into the depths of the human experience. These cinematic masterpieces focus on serious, realistic, and emotionally engaging stories, exploring the intricate tapestry of human relationships, personal struggles, and significant life events. Dramas aim to evoke strong emotional responses from the audience—empathy, sadness, joy, or tension—by delving into the complexities of their characters and the experiences that shape them.

In the realm of drama, every frame is a canvas for exploring the human condition. Filmmakers craft narratives that resonate with universal themes, drawing us into the lives of their characters and making us feel their triumphs and tragedies as our own. Whether it's the heart-wrenching tale of a love lost, the inspiring story of overcoming adversity, or the poignant exploration of family dynamics, dramas have the power to touch our souls and leave an indelible mark on our hearts.

The drama genre is a testament to the power of storytelling, a celebration of the human spirit, and a mirror held up to our own lives. With each film, dramas remind us of our shared humanity, our capacity for love and loss, and our unwavering resilience in the face of life's challenges.

As we continue to explore the vast landscape of cinema, let us remember the enduring appeal of the drama genre—a genre that, with 4361 movies and counting, has proven its ability to captivate, inspire, and move us in ways that no other form of art can.
""")

# Drama per year

st.subheader(":red[Number of Drama movies per year]", divider="red")

drama_movies = movies[movies['genres'].str.contains('Drama')]
drama_movies_per_year = drama_movies['year'].value_counts().sort_index()
st.bar_chart(drama_movies_per_year, color="#FF5555")

st.divider()

# Ratings per year and per month

ratings["dates"] = pd.to_datetime(ratings['timestamp'], unit='s')
ratings['year'] = ratings['dates'].dt.year
ratings['month'] = ratings['dates'].dt.month

st.subheader(":red[Number of ratings per year]", divider="red")
ratings_per_year = ratings['year'].value_counts().sort_index()
st.bar_chart(ratings_per_year, color="#00CC00")

months = st.tabs(["January", "February", "March", "April", "May", "June", "July",
                  "August", "September", "October", "November", "December"])

months_str = ["January", "February", "March", "April", "May", "June", "July",
              "August", "September", "October", "November", "December"]

months_color = ["#FF5555", "#FFAA00", "#FFFF00", "#AAFF00", "#55FF00", "#00FF00",
                "#00FF55", "#00FFAA", "#00FFFF", "#00AAFF", "#0055FF", "#0000FF"]

for month in months:
    with month:
        st.subheader(
            f":red[Number of ratings in {months_str[months.index(month)]}]", divider="red")
        ratings_per_month = ratings[ratings['month'] == months.index(
            month) + 1]['year'].value_counts().sort_index()
        st.bar_chart(ratings_per_month,
                     color=months_color[months.index(month)])

st.write("""
As we explore the dynamic world of cinema through the lens of viewer ratings, we encounter a fascinating journey of peaks and valleys, reflecting the ever-changing landscape of audience engagement.

The turn of the millennium brought about a digital revolution, with the internet becoming more accessible and user-friendly. This shift enabled movie enthusiasts to share their opinions and ratings online with unprecedented ease, leading to a surge in viewer-generated
content.

The late 1990s and early 2000s saw the rise of dedicated movie review websites and online forums. Platforms like IMDb, Rotten Tomatoes, and Metacritic emerged as hubs for movie ratings and reviews, drawing in vast numbers of viewers who were eager to contribute their
insights and opinions.

The turn of the millennium was also marked by a series of cultural phenomena that captivated global audiences. Blockbuster films like "The Matrix," "Titanic," and "Star Wars: Episode I - The Phantom Menace" generated immense hype and discussion, driving viewers to rate and
review these movies in droves.

However, following this peak, there is a significant decline in the number of ratings. This drop could be attributed to several factors that reshaped the cinematic landscape.

As the new millennium progressed, viewing habits began to evolve. The rise of streaming services and digital downloads offered audiences alternative ways to consume content, shifting focus away from traditional rating platforms.

Some platforms may have implemented changes in their policies or algorithms, affecting how viewer ratings were collected, displayed, or weighted. These changes could have temporarily reduced the number of visible ratings.

Despite this decline, the graph shows a resurgence in ratings in the mid-2010s, culminating in another peak around 2017. This uptick can be linked to several contemporary influences.

The rise of social media platforms like Facebook, Twitter, and Instagram transformed how audiences engage with and discuss movies. These platforms facilitated real-time conversations and reviews, drawing viewers back to rating platforms to share their thoughts.

The late 2010s witnessed the emergence of major streaming services, each vying for a piece of the market. This intense competition led to a proliferation of high-quality content, driving audiences to rate and review the latest releases.

The mid-2010s also saw the release of several films that sparked significant cultural conversations. Movies like "Black Panther," "Get Out," and "Parasite" not only entertained but also challenged viewers, inspiring them to engage in thoughtful discussions and ratings.

And so, the journey of cinema continues, a tapestry woven with the threads of technology, culture, and human connection, forever evolving, forever engaging.
""")

st.divider()

st.subheader(":red[Number of movies per tag]", divider="red")

fig = alt.Chart(tags['tag'].value_counts().head(30).reset_index()).mark_bar().encode(
    x='count',
    y=alt.Y('tag', sort='-x'),
    color='tag'
)
st.altair_chart(fig, use_container_width=True)

st.write("""
The world of cinema is a vast and diverse landscape, shaped by the myriad themes and genres that captivate viewers. Each tag represents a unique aspect of a film, drawing in audiences who seek specific experiences and emotional resonances.

One of the most prominent tags is "Disney," which has become synonymous with family-friendly entertainment and timeless classics that span generations. These films often feature beloved characters and enchanting stories that continue to captivate audiences of all ages. From animated adventures to live-action remakes, Disney movies offer a sense of magic and wonder that transcends age and cultural boundaries.

"In Netflix queue" is another significant tag, reflecting the immense popularity of streaming services. With the convenience of on-demand viewing, many films find their way into viewers' Netflix queues, waiting to be enjoyed at a moment's notice. This tag highlights the shift in how audiences consume media, moving away from traditional theater experiences and embracing the flexibility of streaming platforms. The ability to curate a personal queue of movies to watch at one's leisure has transformed the viewing experience for millions of people worldwide.

"Atmospheric" films create immersive worlds that envelop viewers in their visual and emotional landscapes. These movies are known for their evocative settings and mood-setting environments, which contribute to the overall cinematic experience. From eerie horror films set in isolated mansions to sweeping period dramas that transport viewers to another era, atmospheric movies offer a sense of immersion that draws audiences in and keeps them engaged from start to finish.

"Thought-provoking" films tackle complex themes and moral dilemmas, encouraging audiences to reflect on broader societal issues and personal beliefs. "Superhero" movies blend action, drama, and spectacle, appealing to a wide range of viewers. "Funny" movies offer laughter and lighthearted moments, providing a welcome escape from everyday life. "Surreal" films challenge conventional storytelling and visual norms, offering unique and thought-provoking experiences that linger in the mind.

Each tag represents a unique window into the human experience. These tags offer a rich and varied landscape of storytelling, providing something for every viewer and every mood.

And so, the journey of cinema continues, a tapestry woven with the threads of technology, culture, and human connection, forever evolving, forever engaging.
""")

st.divider()

st.subheader(":red[Credits]", divider="red")

st.write("""
As we conclude our journey through the captivating world of cinema, we are reminded of the profound impact that films have on our lives. From the enchanting worlds of Disney to the thought-provoking narratives that challenge our perceptions, the diversity of cinematic experiences lets us think about the power of storytelling through cinema.

The tags that categorize these films are more than just labels; they are windows into the human experience, offering us a chance to explore the depths of our emotions, our dreams, and our collective history. Whether we seek laughter, tears, or intellectual stimulation, the world of cinema provides a rich tapestry of stories that resonate with our souls.

The evolution of film technology, the rise of streaming services, and the enduring allure of the silver screen have all contributed to the vibrant landscape we see today. As we look to the future, we can only imagine the new worlds that will be created, the new stories that will be told, and the new emotions that will be stirred.

Cinema is not just a form of entertainment; it is a mirror held up to society, reflecting our hopes, our fears, and our dreams. It is a medium that transcends language and culture, uniting people from all walks of life in a shared human experience.

As we turn the page on this documentary, let us celebrate the art of filmmaking. Let us continue to support the creators who dare to dream, to challenge, and to inspire. For in every frame, in every tag, and in every story lies the promise of a journey that will touch our hearts and expand our minds.

Thank you for joining us on this cinematic adventure. Until our next journey, keep exploring, keep dreaming, and keep watching the magic unfold on the silver screen.
""")