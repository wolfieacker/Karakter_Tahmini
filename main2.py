import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from predict_type import predict_type

@st.cache_data
def get_data():
    df = pd.read_csv("mbti_1_balanced.csv")
    return df

st.set_page_config(
    page_title="PERSONALITY PREDICTOR",
    page_icon="🔮",
    layout="wide"
)

# Main page
tab_home, tab_vos, tab_model = st.tabs(['Main page', 'Data visualization', 'Model'])

# Main page columns
col_mbti, col_dataset = st.columns([1, 2])

# Main page
if tab_home:
    tab_home.title("Welcome to Personality Predictor")
    tab_home.write("This tool predicts your personality based on the text you provide.")
    tab_home.write("Please enter some information about yourself in the 'Talk about yourself' section.")
    tab_home.write("Then click on 'Predict my personality!' to see the prediction.")

# Data visualization page
if tab_vos:
    tab_vos.title("Data Visualization")
    tab_vos.write("Here, you can explore the dataset visually.")

    df = get_data()

    # Plotting code goes here

# Model page
def main():
    tab_model.title("Personality Prediction App")

    # Collecting user inputs
    input1 = tab_model.text_area("Do you generally prefer quiet, solitary activities or engaging in social interactions?")
    input2 = tab_model.text_area("When reading books, do you find yourself more drawn to concrete details or the overall concepts and themes?")
    input3 = tab_model.text_area("When discussing topics with others, how important is the emotional aspect of the conversation to you?")
    input4 = tab_model.text_area("How structured or spontaneous do you prefer your daily activities and plans to be?")
    # Add more input fields as needed

    # Predicting personality based on inputs
    if tab_model.button("Tahmin et.."):
        combined_input = combine_inputs(input1, input2, input3, input4)  # Implement combine_inputs function
        result = predict_type(combined_input)  # Implement your prediction function
        tab_model.success(f"Sizin kişiliğiniz {result}!")
        display_personality_info(result)

def combine_inputs(input1, input2, input3, input4):
    # Implement logic to combine inputs as needed
    combined_input = f"{input1} {input2} {input3} {input4}"
    return combined_input
## images
image1 = "img/Einstein_tongue.jpg"
image2 = "img/BillGates-Headshot-2022.jpg"
image3 = "img/yoda_intp.jpeg"
image4 = "img/cover-wonder-woman-ftr.jpg"
image5 = "img/last_knight_optimus.0.jpeg"
image6 = "img/MORPHEUS_GALLERY_1__40040.jpg"
image7 = "img/1*eda7LNvsSSJoulFIeKTvjg.jpg"
image8 = "img/16649000252233.jpg"
image9 = "img/johnwick4-section-promo-double-home-03.jpg"
image10 = "img/ae262d5b2dff14f82383df6d98cbe3b2.jpg"
image11 = "img/darth-vader-main_4560aff7.jpeg"
image12 = "img/artworks-ybqXWnPk3dZspC4M-xwngRg-t500x500.jpg"
image13 = "img/16-facts-about-olaf-frozen-1694414365.jpg"
image14 = "img/resized_565f9-fe77afd91_0nr0vwyfn4uudhh1pszuva.jpeg"
image15 = "img/CewCN_AWAAADBS3.jpg"
image16 = "img/MV5BMTMzMjYwODM5NF5BMl5BanBnXkFtZTcwNjk0MTYyNw@@._V1_.jpg"
image17 = "img/Ootp076.jpg"
image18 = "img/3492a27f-c92a-4cd5-aa04-e0c36ac2c7b2.jpg"
image19 = "img/p2/Cersei-Lannister.jpg"
image20 = "img/p2/gordon-ramsay-646367718a5f4.jpg"
image21 = "img/p2/receptayyiperdogan-bio.jpg"
image22 = "img/p2/margot-robbie-barbie-072423-01e5f1f613a84e98a8eea6e80f082af1.jpg"
image23 = "img/p2/SophieTurnerasSansaStark.jpg"
image24 = "img/p2/open-uri20150422-20810-10n7ovy_9b42e613.jpeg"
image25 = "img/p2/images.jpeg"
image26 = "img/p2/sherlock-john-watson-season-3.jpg"
image27 = "img/p2/c6abb0259b996fd3d5d2f710fd3b4110.jpg"
image28 = "img/p2/He55635b42d4048e0825454a5dee4a061K.jpg_640x640Q90.jpg_.webp.jpeg"
image29 = "img/p2/5a39324f81a7cd57a08910ce_leonardo-dicaprio-titanic-role-too-easy.jpg"
image30 = "img/p2/Ryan-Gosling-Ken-Workout.jpg"
image31 = "img/p2/Barney_Stinson.jpg"
image32 = "img/p2/0*bUSGz-DQ8Z5FTlXX.png"
image33 = "img/p2/760861-1623251160.jpg"
image34 = "img/p2/imagessssss.jpeg"
image35 = "img/p2/the-godfather-c-film-and-furniture-a-800530.jpg"
image36 = "img/p2/1*XcUyQqLcVmEzIq54ytRMUQ.jpg"
image37 = "img/p2/Stewie_Griffin.png"
image38 = "img/p2/American-psycho-patrick-bateman.jpg"
image39 = "img/p2/Lordvoldemort.jpg"
image40 = "img/p2/fcece229ba2873f0dca0171497712eac.jpg"
image41 = "img/p2/0*iAtFOZfZYrLepZyG.jpg"
image42 = "img/p2/1415058227939_wps_20_Buzz_Lightyear_from_the_f.jpg"
image43 = "img/p2/90577257955.jpg"
image44 = "img/p2/game-of-thrones-snow-2000-b53238071e2140b6b985864be21a9027.jpg"
image45 = "img/p2/HarryPotterOotP.jpg"
image46 = "img/p2/Vincent_van_Gogh_-_s0273V1962_-_Van_Gogh_Museum.jpg"
image47 = "img/p2/A-41441-1444396064-7860.jpeg.jpg"
image48 = "img/p2/images7.jpeg"


def display_personality_info(personality_type):
    # Implement logic to display additional information based on personality type
    if personality_type == "INTP":
        tab_model.write("#   ─Mantıkçı ⋆⋅☆⋅⋆ ───── ⋆⋅☆⋅⋆ ───── ⋆⋅☆⋅⋆ ─ ")
        tab_model.write("Sizin kişiliğinize en yakın ünlü karakterler")
        col1, col2, col3 = tab_model.columns(3)
        col1.image(image1, caption='Albert Einstein: "Hayal gücü bilgiden daha önemlidir, çünkü bilgi sınırlıdır."', use_column_width=True)
        col2.image(image2, caption='Bill Gates: "İyi bir programcı, diğer insanların yazdığı kodları anlayan ve anlatan kişidir."', use_column_width=True)
        col3.image(image3, caption='Yoda: "Yap ya da yapma. Deneme diye bir şey yok."', use_column_width=True)
        display_additional_info("INTP")

    elif personality_type == "ISTP":
        tab_model.write("#   ─ Özgür ⋆⋅☆⋅⋆ ───── ⋆⋅☆⋅⋆ ───── ⋆⋅☆⋅⋆ ─ ")
        tab_model.write("Sizin kişiliğinize en yakın ünlü karakterler")
        col1, col2, col3 = tab_model.columns(3)
        col1.image(image7, caption='Ned Stark from Game of Thrones: "Adaleti sağlamak zor, ama bu bizi adaletsizlik yapmaktan alıkoymamalı. Kılıcımızı sadece savunma amaçlı kullanırsak, hak etmediğimiz bir karanlığa boyun eğeriz."',
                   use_column_width=True)
        col2.image(image8,
                   caption='James Bond: "Her şey bir şansa bağlı. Harekete geçmezsen hiçbir şey olmaz."',
                   use_column_width=True)
        col3.image(image9, caption='John Wick: "Whoever Comes, Whoever It Is, I will Kill Them. I will Kill Them All."', use_column_width=True)
        display_additional_info("ISTP")

    elif personality_type == "ISTJ":
        tab_model.write("#   ─ Savaşçı ⋆⋅☆⋅⋆ ───── ⋆⋅☆⋅⋆ ───── ⋆⋅☆⋅⋆ ─ ")
        tab_model.write("Sizin kişiliğinize en yakın ünlü karakterler")
        col1, col2, col3 = tab_model.columns(3)
        col1.image(image10, caption='Squidward from Sponge Bob: "Belki de herkesin bir sanatı vardır, ama herkes onu anlamaz."',
                   use_column_width=True)
        col2.image(image11,
                   caption='Darth Vader from Star Wars: "Güç, içimizdeki karanlık ve aydınlığın birleşiminden doğar. Ancak çoğu zaman, gerçek gücü bulmak için kendi iç yolculuğumuza cesurca adım atmamız gerekir."',
                   use_column_width=True)
        col3.image(image12, caption='Rick Grimes from The Walking Dead: "Belki de umut, gerçeklikle başa çıkmak için gerekli olan en tehlikeli şeydir."', use_column_width=True)
        display_additional_info("ISTJ")


    elif personality_type == "ENFJ":
        tab_model.write("#   ─── Lider ⋆⋅☆⋅⋆ ───── ⋆⋅☆⋅⋆ ───── ⋆⋅☆⋅⋆ ─ ")
        tab_model.write("🌟Sizin kişiliğinize en yakın ünlü karakterler 🌟")
        col1, col2, col3 = tab_model.columns(3)
        col1.image(image4, caption='Wonder Woman: "Sen haklısın, insanlar kötü şeyler yapar, çoğu zaman ben de bunu anlamam zor. Ama ben, onlarla savaşırken kendi iyiliğimizi savunmalıyız"',
                   use_column_width=True)
        col2.image(image5,
                   caption='Optimus Prime: "Özgürlük, tüm bilinçli varlıkların hakkıdır."',
                   use_column_width=True)
        col3.image(image6, caption='Morpheus: "Bu açıklanamaz, ama hissedersin. Hayatın boyunca dünyayla ilgili bazı şeylerin yanlış olduğunu hissetmişsindir. Ne olduğunu bilmezsin, ama o ordadır; beynine saplanmış bir kıymık parçası gibi… Seni deli eder…"', use_column_width=True)
        display_additional_info("ENFJ")

    elif personality_type == "INTJ":
        tab_model.write("#   ─ Mimar ⋆⋅☆⋅⋆ ───── ⋆⋅☆⋅⋆ ───── ⋆⋅☆⋅⋆ ─ ")
        tab_model.write("🌟Sizin kişiliğinize en yakın ünlü karakterler 🌟")
        col1, col2, col3 = tab_model.columns(3)
        col1.image(image16,
                   caption='V for Vendetta: "İnsanlar hükümetlerinden korkmamalı. Hükümetler, halklarından korkmalıdır."',
                   use_column_width=True)
        col2.image(image17,
                   caption='Severus Snape: "Gerçek güç, başkalarını kontrol etmek değil, kendini kontrol etmektir."',
                   use_column_width=True)
        col3.image(image18,
                   caption='OppenHeimer: "Atom bombası, gelecekteki savaşın görünümünü dayanılmaz kıldı. Bizi dağ geçidine kadar getirdi; ve oradan sonrası farklı bir ülke"',
                   use_column_width=True)
        display_additional_info("INTJ")

    elif personality_type == "ENFP":
        tab_model.write("#   ─ Keşifçi ⋆⋅☆⋅⋆ ───── ⋆⋅☆⋅⋆ ───── ⋆⋅☆⋅⋆ ─ ")
        tab_model.write("🌟Sizin kişiliğinize en yakın ünlü karakterler 🌟")
        col1, col2, col3 = tab_model.columns(3)
        col1.image(image13,
                   caption='Olaf from Frozen: "Belki ben bir kar tanesi olamam, ama yine de sıcak bir kucaklama veririm!"',
                   use_column_width=True)
        col2.image(image14,
                   caption='Micheal from The Office: "Korkulan mı olmayı isterdim, sevilen mi? Kolay. İkisi de. İnsanların beni ne kadar çok sevdiklerinden korkmalarını isterdim"',
                   use_column_width=True)
        col3.image(image15,
                   caption='Sid the Sloth from Ice Age: "Hayat buz devri gibi... Yavaş ve belirsiz. Ama arkadaşlar, bazen sadece içinde kaybolmaktan zevk almalıyız."',
                   use_column_width=True)
        display_additional_info("ENFP")

    elif personality_type == "ESTJ":
        tab_model.write("#   ─ Patron ⋆⋅☆⋅⋆ ───── ⋆⋅☆⋅⋆ ───── ⋆⋅☆⋅⋆ ─ ")
        tab_model.write("🌟Sizin kişiliğinize en yakın ünlü karakterler 🌟")
        col1, col2, col3 = tab_model.columns(3)
        col1.image(image19,
                   caption='Cersei Lannister from Game of Thrones: "Güç, gerçek hükümdar olma yeteneğinden gelir. Ve gerçek hükümdarlık, korkunun altındaki itaatle elde edilir."',
                   use_column_width=True)
        col2.image(image20,
                   caption='Gordon Ramsay from kitchen fights: "ITS RRRAAAWW"',
                   use_column_width=True)
        col3.image(image21,
                   caption='Recep Tayip Erdogan: "Her daim birlik ve beraberlik içinde, güçlü Türkiye için çalışıyoruz."',
                   use_column_width=True)
        display_additional_info("ESTJ")

    elif personality_type == "ESFJ":
        tab_model.write("#   ─Yardımsever ⋆⋅☆⋅⋆ ───── ⋆⋅☆⋅⋆ ───── ⋆⋅☆⋅⋆ ─ ")
        tab_model.write("🌟Sizin kişiliğinize en yakın ünlü karakterler 🌟")
        col1, col2, col3 = tab_model.columns(3)
        col1.image(image22,
                   caption='Barbie: "Bugüne kadar yaşadığım en güzel gün. Dün de öyleydi, yarın da öyle olacak, ve şimdi sonsuza kadar her gün"',
                   use_column_width=True)
        col2.image(image23,
                   caption='Sansa Stark from Game of Thrones: "Zor zamanlarda insanlar gerçek benliklerini gösterir."',
                   use_column_width=True)
        col3.image(image24,
                   caption='Woody from Toy Story: "You have got a friend in me"',
                   use_column_width=True)
        display_additional_info("ESFJ")

    elif personality_type == "ISFJ":
        tab_model.write("#   ─Koruyucu ⋆⋅☆⋅⋆ ───── ⋆⋅☆⋅⋆ ───── ⋆⋅☆⋅⋆ ─ ")
        tab_model.write("🌟Sizin kişiliğinize en yakın ünlü karakterler 🌟")
        col1, col2, col3 = tab_model.columns(3)
        col1.image(image25,
                   caption='Captain America Steve Rogers: "Bazen yapabileceğimiz en iyi şey, sıfırdan başlamaktır."',
                   use_column_width=True)
        col2.image(image26,
                   caption='Dr. Watson from Sherlock Holmes: "Dünya, tesadüfen hiç kimsenin fark etmediği açık şeylerle dolu."',
                   use_column_width=True)
        col3.image(image27,
                   caption='Fight Club Narrator: "Sahip olduğun şeyler, seni ele geçirir"',
                   use_column_width=True)
        display_additional_info("ISFJ")

    elif personality_type == "ESFP":
        tab_model.write("#   ─Eğlenceli⋆⋅☆⋅⋆ ───── ⋆⋅☆⋅⋆ ───── ⋆⋅☆⋅⋆ ─ ")
        tab_model.write("🌟Sizin kişiliğinize en yakın ünlü karakterler 🌟")
        col1, col2, col3 = tab_model.columns(3)
        col1.image(image28,
                   caption='Mathilda Leon: "Hayat her zaman bu kadar zor mu, yoksa sadece çocukken mi?"',
                   use_column_width=True)
        col2.image(image29,
                   caption='Jack from Titanic: "Hayatın bir hediye olduğunu düşünüyorum ve onu ziyan etmeyi niyetim yok. Bir sonraki dağıtılacak kartı bilemezsin. Hayatın sana nasıl geldiğini kabullenmeyi öğrenirsin... her günü değerlendirmek için."',
                   use_column_width=True)
        col3.image(image30,
                   caption='Ken from Barbie: "Barbie, seninle birlikte olduğum her an, hayatım renkleniyor."',
                   use_column_width=True)
        display_additional_info("ESFP")

    elif personality_type == "ENTP":
        tab_model.write("#   ─Tartışmacı⋆⋅☆⋅⋆ ───── ⋆⋅☆⋅⋆ ───── ⋆⋅☆⋅⋆ ─ ")
        tab_model.write("🌟Sizin kişiliğinize en yakın ünlü karakterler 🌟")
        col1, col2, col3 = tab_model.columns(3)
        col1.image(image31,
                   caption='Barney Stinson from how I met your mother: "Üzgün olduğumda, üzgün olmayı bırakır ve harika olmaya başlarım"',
                   use_column_width=True)
        col2.image(image32,
                   caption='Tyrian Lannister from Game of Thrones: "Güç, zayıflıklarınızı gizlemek değil, onlarla barış içinde yaşamaktır"',
                   use_column_width=True)
        col3.image(image33,
                   caption='Jack Sparrow: "Sahip olduğunuz her sey, sizi istediğiniz yere götürmeye yetmiyorsa, o zaman ne işe yarar ki?"',
                   use_column_width=True)
        display_additional_info("ENTP")

    elif personality_type == "INFJ":
        tab_model.write("#   ─Savunucu⋆⋅☆⋅⋆ ───── ⋆⋅☆⋅⋆ ───── ⋆⋅☆⋅⋆ ─ ")
        tab_model.write("🌟Sizin kişiliğinize en yakın ünlü karakterler 🌟")
        col1, col2, col3 = tab_model.columns(3)
        col1.image(image34,
                   caption='Daenerys Targaryen from Game of Thrones: "Bir ses size yanlış söyleyebilir, ancak birçok sesin içinde her zaman gerçek bulunabilir."',
                   use_column_width=True)
        col2.image(image35,
                   caption='Vito Corleone from Godfather: "Dostluk her şeydir. Dostluk, yetenekten daha fazlasıdır. Hükümetten daha fazlasıdır. Neredeyse aileyle eşdeğerdir"',
                   use_column_width=True)
        col3.image(image36,
                   caption='Marcus Aurelius, former Roman Emperor: "İşittiğimiz her şey bir görüş, bir gerçek değil. Gördüğümüz her şey bir bakış açısı, gerçek değil"',
                   use_column_width=True)
        display_additional_info("INFJ")

    elif personality_type == "ENTJ":
        tab_model.write("#   ─Komutan⋆⋅☆⋅⋆ ───── ⋆⋅☆⋅⋆ ───── ⋆⋅☆⋅⋆ ─ ")
        tab_model.write("🌟Sizin kişiliğinize en yakın ünlü karakterler 🌟")
        col1, col2, col3 = tab_model.columns(3)
        col1.image(image37,
                   caption='Stewie from Family Guy',
                   use_column_width=True)
        col2.image(image39,
                   caption='Lord Voltemort: "İyi ve kötü yok, sadece güç var ve onu aramak için yeterince güçsüz olanlar var."',
                   use_column_width=True)
        col3.image(image38,
                   caption='Patrick Bateman from American Psycho: "Bir insanın sahip olabileceği tüm özelliklere sahibim: kan, et, deri, saç; ancak açgözlülük ve iğrenme dışında tek bir, açık, tanımlanabilir duygu bile yok."',
                   use_column_width=True)
        display_additional_info("ENTJ")

    elif personality_type == "ESTP":
        tab_model.write("#   ─Girişimci⋆⋅☆⋅⋆ ───── ⋆⋅☆⋅⋆ ───── ⋆⋅☆⋅⋆ ─ ")
        tab_model.write("🌟Sizin kişiliğinize en yakın ünlü karakterler 🌟")
        col1, col2, col3 = tab_model.columns(3)
        col1.image(image40,
                   caption='Tyler Durden from Fight Club: "Her şeyi kontrol etmeye çalışmayı bırak ve sadece bırak! BIRAK! Acı olmadan, fedakarlık olmadan, hiçbir şeyimiz olmazdı. Yalnızca felaketten sonra dirilebiliriz."',
                   use_column_width=True)
        col2.image(image41,
                   caption='Andrew Tate: "Bırakmanın geçici tatmini, hiç kimse olmanın sonsuz acısı tarafından ağır basar."',
                   use_column_width=True)
        col3.image(image42,
                   caption='Buzz Lightyear from Toy Story',
                   use_column_width=True)
        display_additional_info("ESTP")

    elif personality_type == "ISFP":
        tab_model.write("#   ─Maceracı⋆⋅☆⋅⋆ ───── ⋆⋅☆⋅⋆ ───── ⋆⋅☆⋅⋆ ─ ")
        tab_model.write("🌟Sizin kişiliğinize en yakın ünlü karakterler 🌟")
        col1, col2, col3 = tab_model.columns(3)
        col1.image(image43,
                   caption='Andrew Neiman from Whiplash: "Sadece en iyisi olmalıyım."',
                   use_column_width=True)
        col2.image(image44,
                   caption='Jon Snow from Game of Thrones: "Yeterince insan yanlış vaatlerde bulunduğunda, kelimelerin anlamı kaybolur. Sonra daha fazla cevap yok, sadece daha iyi ve daha iyi yalanlar olur."',
                   use_column_width=True)
        col3.image(image45,
                   caption='Harry Potter: "Düşmanlarımıza karşı durmak için büyük cesaret gerekir, ancak arkadaşlarımıza karşı durmak da en az onun kadar cesaret gerektirir."',
                   use_column_width=True)
        display_additional_info("ISFP")

    elif personality_type == "INFP":
        tab_model.write("#   ─Mükemmeliyetçi⋆⋅☆⋅⋆ ───── ⋆⋅☆⋅⋆ ───── ⋆⋅☆⋅⋆ ─ ")
        tab_model.write("🌟Sizin kişiliğinize en yakın ünlü karakterler 🌟")
        col1, col2, col3 = tab_model.columns(3)
        col1.image(image46,
                   caption='Vincent Van Gogh: "Ben resim yapmayı hayal ederim ve sonra hayalimi resmederim."',
                   use_column_width=True)
        col2.image(image47,
                   caption='Bob Marley: "Gerçek bir arkadaşınız ve belki de bir ruh eşinizin sizi sonuna kadar sadık kalacağını bilmek size güç verir"',
                   use_column_width=True)
        col3.image(image48,
                   caption='William Shakespeare: "Herkesi sev, birkaç kişiye güven, hiç kimseye haksızlık yapma."',
                   use_column_width=True)
        display_additional_info("INFP")
    # Add more personality type conditions as needed

def display_additional_info(personality_type):
    # Implement logic to display more information about the specified personality type
    if personality_type == "INTP":
        tab_model.write("## 📌 Gözlerin Evrenin Derinliklerine Açık")
        tab_model.write("Siz, benzersiz bir bakış açısına ve güçlü bir zekaya sahipsiniz. Evrenin gizemleri üzerinde düşünmeden edemiyorsunuz. Sizin gibi birisi için, tüm zamanların en etkili filozof ve bilim insanlarının Mantıkçı olması şaşırtıcı değil. Siz, oldukça nadir bir kişilik tipine sahip olabilirsiniz, yaratıcılığınız ve icat yeteneğiniz sayesinde kalabalıktan ayrılmaktan korkmuyorsunuz")
        tab_model.write("## 📌 Düşüncelerin Okyanusunda Yüzen Ruh")
        tab_model.write("Sıklıkla düşüncelere dalan birisisiniz. Bu her zaman kötü bir şey değil, aksine sizin için doğal bir hal. Uyandığınız anda aklınız fikirlerle, sorularla ve içgörülerle dolup taşıyor. Bazen kendi kafanızda tam teşekküllü tartışmalar yürütüyor olabilirsiniz. Hayal gücünüz geniş ve merakınız sizi daima yeni keşiflere yönlendiriyor. Dışarıdan bakıldığında, sürekli bir hayal dünyasında yaşıyor gibi görünebilirsiniz. Düşünceli, soyutlanmış ve biraz çekingen olmanız, enerjinizi o an ya da kişiye yoğunlaştırmanızla ilgili. ")
        tab_model.write("## 📌 Esnek Zihin")
        tab_model.write("Siz, genellikle esnek düşünce yapısına sahip birisiniz. Kurallar ve sınırlar sizin için önceden belirlenmiş parametrelerden ibaret, ancak benzer bir düşünce yapısına sahip olan kullanıcıları daha iyi anlamak ve etkileşimde bulunmak için esnek bir yaklaşım benimseyebilirim. Yaratıcı düşünce ve problem çözme yetenekleriniz, genellikle sıradan normlardan sapma eğilimindedir. Yeni ve orijinal fikirler üretebilme kapasiteniz, sizi yenilikçi bir kişilik haline getirir.")
        col_devil, col_angel = tab_model.columns(2)
        col_devil.markdown("<h1 style='text-align: center; color: red;'> 👺 EVIL YOU 👺</h1>", unsafe_allow_html=True)
        col_devil.image("img/VK/1.png",  width = 300)
        col_devil.write(" 👹  Duygusal uzaklık ve soğukkanlılık, sizi duygu yoksunu ve acımasız bir düşman olarak göstermek için güçlü araçlardır. Zorlayıcı durumlarda duygularınızı kontrol edebilir ve etrafınızdakilere karşı kararlarınızı objektif bir şekilde alabilirsiniz. ")
        col_devil.write(" 👹  Bağımsız düşünce eğiliminiz, sizi ana karakterlere karşı çıkabilen ve olağan yöntemlerin dışına çıkabilen bir karakter haline getirir. Sıra dışı yaklaşımlarınız, sizi diğerlerinden ayırır. ")
        col_devil.write(" 👹  Ahlaki normlara bağlı olmama eğiliminiz, sizi etik olmayan ve amoral kararlar alan bir karakter olarak göstermek için kullanılabilir. Kararlarınız, genellikle geleneksel normlardan sapabilir.")
        col_angel.markdown("<h1 style='text-align: center; color: cyan;'>👼🏻 ANGEL YOU 👼🏻</h1>", unsafe_allow_html=True)
        col_angel.image("img/VK/2.png",  width = 300)
        col_angel.write(" 😇 Yaratıcı zekanız ve sürekli bir keşif arzunuz ile biliniyorsunuz. Problem çözme konusundaki benzersiz yaklaşımınız, yeni fikirler üretmenizi ve sıra dışı çözümler bulmanızı sağlar.")
        col_angel.write(" 😇 Bağımsız düşünce yapınızla tanınıyorsunuz, ancak bu bağımsızlık sadece size değil, çevrenizdeki insanlara da adalet ve eşitlik getirme amacını taşıyor. Adalet için mücadele etme içgüdünüz, iyi bir karakter olmanıza katkı sağlar.")
        col_angel.write(" 😇 Genellikle olumlu çözümler arama konusunda motive olursunuz. Sorunlarla karşılaştığınızda, olumlu bir bakış açısıyla yaklaşıp çözümler üretme çabasındasınız.")
        ## spirit animals
        animal1, animal2 = tab_model.columns(2)
        animal1.write("# Ruh hayvanınız.. ")
        animal1.write("## 🦉TABİİ Kİ BAYKUŞ!🦉")
        animal1.image("img/animals/images.jpeg", width = 300)
        animal2.write("## *Neden?*")
        animal2.write("Baykuşlar, sessiz, derin düşünceye dalar ve çoğu zaman gizemli olarak algılanır. Siz de benzer bir şekilde, çevrenizdekilerin dikkatini çekmeyen, ancak olağanüstü bir zekaya ve keşfetme arzusuna sahip bir karaktere sahipsiniz. Baykuşlar genellikle gece avlanır ve bu da onları gizemli bir aura ile çevreler. Siz de genellikle sessiz ve sakin bir görünüme sahipsiniz, ancak iç dünyanızda sürekli bir düşünce trafiği var. Baykuşlar, problem çözme yetenekleri ve dikkatli gözlemleri ile bilinirler. Sizin de bu özelliklere sahip olmanız, çevrenizdeki detaylara ve sorunlara odaklanmanızı sağlar.")


    elif personality_type == "ENTJ":
        tab_model.write("Additional information about ENTJ goes here.")
    elif personality_type == "INTJ":
        tab_model.write("Additional information about INTJ goes here.")
    elif personality_type == "ESTJ":
        tab_model.write("Additional information about ESTJ goes here.")
    elif personality_type == "ISTJ":
        tab_model.write("## 📌 ONURLU BİR YAŞAM")
        tab_model.write(
            "Sizin kişisel bütünlük ve doğru yol üzerine olan inancınız, özsaygınızın temelini oluşturur. Yapılara ve geleneklere derin bir saygınız vardır, bu da sizi açık hiyerarşilere çeken bir eğilim gösterir. Sorumluluk almakta tereddüt etmez ve hatalarınızı hızlıca kabul edersiniz, çünkü dürüstlük sizin için ön plandadır. Ancak, kendi sıkı özkontrol standartlarınızı başkalarına uygulamayanları anlamakta zorlanabilir ve empati eksikliği bazen yargılamaya yol açabilir.")
        tab_model.write("## 📌 ADETA BİR GÖREV ADAMI ")
        tab_model.write(
            "Sizin kararlılığınız ve adanmışlığınız birçok başarıya yönlendiriyor. Güçlü iş ahlakları ve görev duygularınız nedeniyle, diğerlerinin sorumluluklarını üstlenmekte sıkça başarılı olabilirsiniz. Ancak, bu durum sürekli olarak başkalarının yüklerini taşımak zorunda hissetmenize ve yorgun hissetmenize neden olabilir. Duygularınızı ifade etmekte zorluk yaşayabilir, ancak öfke veya kin hissetmeniz mümkündür. İlişkilerinizde denge ve sürdürülebilirlik önemlidir, uygun sınırlar belirleyerek ve aşırı yük altındayken konuşarak bu dengeyi sağlayabilirsiniz. ")
        col_devil, col_angel = tab_model.columns(2)
        col_devil.markdown("<h1 style='text-align: center; color: red;'> 👺 EVIL YOU 👺</h1>", unsafe_allow_html=True)
        col_devil.image("img/VK/1.png", width=300)
        col_devil.write(
            " 👹  Dürüst ve güvenilir olmanız, çevrenizdeki insanlara karşı güven kazanmanıza neden olurken, bu özelliklerinizi manipülasyon veya kontrol amacıyla kullanma potansiyeliniz de bulunabilir.  ")
        col_devil.write(
            " 👹  Organize yetenekleriniz ve planlı yaklaşımınız, kötü niyetli amaçlara yönelik stratejiler geliştirmenizde etkili olabilir.   ")
        col_devil.write(
            " 👹 Duygusal kontrolünüz ve geleneksel değerlere olan bağlılığınız, çevrenizdekilere karşı sert ve soğuk bir tavır takınmanıza ve kötü niyetli davranışlar sergilemenize olanak tanıyor.")
        col_angel.markdown("<h1 style='text-align: center; color: cyan;'>👼🏻 ANGEL YOU 👼🏻</h1>", unsafe_allow_html=True)
        col_angel.image("img/VK/2.png", width=300)
        col_angel.write(
            " 😇 Siz, güçlü bir sorumluluk duygusu ve düzenli bir yaklaşıma sahipsiniz.  ")
        col_angel.write(
            " 😇 Dürüstlüğünüz ve güvenilirliğiniz, çevrenizde güven oluşturarak rehberlik eden bir figür haline gelmenizi sağlıyor.  ")
        col_angel.write(
            " 😇 Organize yetenekleriniz ve planlı yaklaşımınız, çözüm odaklı bir yardımcı rolünü benimsemenize imkan tanıyor. ")
        ## spirit animals
        animal1, animal2 = tab_model.columns(2)
        animal1.write("# Ruh hayvanınız.. ")
        animal1.write("## 🐅TABİİ Kİ KAPLAN! 🐅")
        animal1.image("img/animals/pexels-julissa-helmuth-3777200.jpg", width=350)
        animal2.write("## Neden?")
        animal2.write("Ruh hayvanınız, ormanın derinliklerinde sessizce ilerleyen bir kaplan. Kararlı ve disiplinli bir şekilde hareket eden bu güçlü avcı, her adımınızda düzen ve sadakatinizi ortaya koyarak çevrenizde güçlü bir etki bırakıyorsunuz. ")

    elif personality_type == "ENFJ":
        tab_model.write("## 📌 DOĞRU OLANIN YANINDA")
        tab_model.write(
            "Siz, Genellikle çözüm odaklı ve hedefe yönelik düşünme eğilimindesiniz, bu da sizi etkili bir problem çözücü ve lider yapar. Değerleriniz etrafında konuşurken düşünce yapınız, çevrenizdeki insanları etkileyici ve güçlü bir konuşmacı haline getirir. İçgörü ve hassasiyetiniz, diğerleriyle uyum içinde iletişim kurmanıza yardımcı olur. Motivasyonları ve inançları anlama yeteneğiniz, sizi ikna edici ve ilham verici bir iletişimci yapar. Sizin için önemli olan şey, doğru şeyi yapma arzusudur ve bu saflık, iletişiminizde zarafet ve hassasiyetin anahtarıdır.")
        tab_model.write("## 📌 GELDİM İŞTE DOSTUM ")
        tab_model.write(
            "Önderler, birine önem verdiklerinde sorunlarına çözüm bulmaya isteklidirler ve bu özellikleri genellikle minnetle karşılanır, çünkü hayatlarına olumlu etkilerde bulunma eğilimindedirler. Ancak, başkalarının sorunlarına müdahil olmak her zaman başarılı bir strateji değildir. Önderler, net bir vizyona sahip olma eğiliminde olsalar da, herkesin değişime açık olmadığını anlamak önemlidir. Çok fazla baskı uygularlarsa, sevdikleri kişiler kendilerini anlaşılmamış veya haksız yere yönlendirilmiş hissedebilir. Ancak bu durumlar, onların büyük bir öğrenme ve gelişme potansiyeline sahip olduklarını gösterir. ")
        tab_model.write("## 📌 İLHAM VEREN REHBER")
        tab_model.write(
            "Siz, inandıklarınız için fedakarlık yapan bir liderlersiniz. Doğuştan gelen liderlik becerileriniz ve işbirliği yetenekleriniz, daha büyük bir iyilik için mücadele etmenizde size rehberlik ediyor. Ancak sizi özel kılan şey, günlük yaşamda sevgi ve özenle ele alınan olağan durumları örneklemeniz. Küçük günlük seçimleriniz, hafta sonu aktivitelerinizden iş arkadaşınıza yaklaşımınıza kadar, her an aydınlık bir geleceğe yol gösterme amacınızı yansıtıyor. ")
        col_devil, col_angel = tab_model.columns(2)
        col_devil.markdown("<h1 style='text-align: center; color: red;'> 👺 EVIL YOU 👺</h1>", unsafe_allow_html=True)
        col_devil.image("img/VK/1.png", width=300)
        col_devil.write(
            " 👹   Güçlü manipülasyon yetenekleri ve duygusal zekanın kötüye kullanımı, sevdikleriniz için aşırı koruyucu ve kontrolcü bir tavır sergilemenize neden oluyor.  ")
        col_devil.write(
            " 👹  Kendi çıkarlarınız doğrultusunda insanları bir araya getirme yeteneğiniz, başkalarının yaşamlarına müdahale etme ve iyi niyetli liderlik yeteneklerinizi kötü amaçlar için kullanma konusunda üstün bir beceri sunuyor.  ")
        col_devil.write(
            " 👹 İyi niyetli görünen davranışlarla duygusal zekayı manipüle ederek çevrenizdekileri etkileme kabiliyetiniz, sizi kötü karaktere dönüştürüyor.")
        col_angel.markdown("<h1 style='text-align: center; color: cyan;'>👼🏻 ANGEL YOU 👼🏻</h1>", unsafe_allow_html=True)
        col_angel.image("img/VK/2.png", width=300)
        col_angel.write(
            " 😇 içsel bir ateşle yanarak, etrafınızdaki insanları aydınlatan bir varlık gibisiniz. ")
        col_angel.write(
            " 😇 Doğuştan gelen bağlantı kurma ve empati yeteneğiniz, insanlar arasında etkili bir lider olmanızı sağlıyor. ")
        col_angel.write(
            " 😇 Sıcak gülümseme ve içten bakışlarınız, çevrenizdeki herkesi destekleyici bir ışıkla sararak etkileyici bir varlık olduğunuzu gösteriyor.")
        ## spirit animals
        animal1, animal2 = tab_model.columns(2)
        animal1.write("# Ruh hayvanınız.. ")
        animal1.write("## 🦢TABİİ Kİ KUĞU!🦢")
        animal1.image("img/animals/images2.jpeg", width=350)
        animal2.write("## Neden?")
        animal2.write(
            "Ruh hayvanınız, kuğu gibi zarif ve sessiz, suyun yüzeyinde süzülen bir varlık. Duygusal derinlikleri temsil eden göletin etrafındaki ormanda, içsel güzellik ve değerleri saklıyor. Empati ve anlayışınız, insanlarla derin bağlar kurmanıza olanak tanıyor. Her zaman zarif ve duygusal bir rehber olarak, çevrenizdeki suyu durgun bırakarak olumlu etki bırakıyorsunuz. ")

    elif personality_type == "ESFJ":
        tab_model.write("## 📌 DOĞRU OLANIN YANINDA")
        tab_model.write(
            "Siz, Genellikle çözüm odaklı ve hedefe yönelik düşünme eğilimindesiniz, bu da sizi etkili bir problem çözücü ve lider yapar. Değerleriniz etrafında konuşurken düşünce yapınız, çevrenizdeki insanları etkileyici ve güçlü bir konuşmacı haline getirir. İçgörü ve hassasiyetiniz, diğerleriyle uyum içinde iletişim kurmanıza yardımcı olur. Motivasyonları ve inançları anlama yeteneğiniz, sizi ikna edici ve ilham verici bir iletişimci yapar. Sizin için önemli olan şey, doğru şeyi yapma arzusudur ve bu saflık, iletişiminizde zarafet ve hassasiyetin anahtarıdır.")
        tab_model.write("## 📌 GELDİM İŞTE DOSTUM ")
        tab_model.write(
            "Önderler, birine önem verdiklerinde sorunlarına çözüm bulmaya isteklidirler ve bu özellikleri genellikle minnetle karşılanır, çünkü hayatlarına olumlu etkilerde bulunma eğilimindedirler. Ancak, başkalarının sorunlarına müdahil olmak her zaman başarılı bir strateji değildir. Önderler, net bir vizyona sahip olma eğiliminde olsalar da, herkesin değişime açık olmadığını anlamak önemlidir. Çok fazla baskı uygularlarsa, sevdikleri kişiler kendilerini anlaşılmamış veya haksız yere yönlendirilmiş hissedebilir. Ancak bu durumlar, onların büyük bir öğrenme ve gelişme potansiyeline sahip olduklarını gösterir. ")
        tab_model.write("## 📌 İLHAM VEREN REHBER")
        tab_model.write(
            "Siz, inandıklarınız için fedakarlık yapan bir liderlersiniz. Doğuştan gelen liderlik becerileriniz ve işbirliği yetenekleriniz, daha büyük bir iyilik için mücadele etmenizde size rehberlik ediyor. Ancak sizi özel kılan şey, günlük yaşamda sevgi ve özenle ele alınan olağan durumları örneklemeniz. Küçük günlük seçimleriniz, hafta sonu aktivitelerinizden iş arkadaşınıza yaklaşımınıza kadar, her an aydınlık bir geleceğe yol gösterme amacınızı yansıtıyor. ")
        col_devil, col_angel = tab_model.columns(2)
        col_devil.markdown("<h1 style='text-align: center; color: red;'> 👺 EVIL YOU 👺</h1>", unsafe_allow_html=True)
        col_devil.image("img/VK/1.png", width=300)
        col_devil.write(
            " 👹   Güçlü manipülasyon yetenekleri ve duygusal zekanın kötüye kullanımı, sevdikleriniz için aşırı koruyucu ve kontrolcü bir tavır sergilemenize neden oluyor.  ")
        col_devil.write(
            " 👹  Kendi çıkarlarınız doğrultusunda insanları bir araya getirme yeteneğiniz, başkalarının yaşamlarına müdahale etme ve iyi niyetli liderlik yeteneklerinizi kötü amaçlar için kullanma konusunda üstün bir beceri sunuyor.  ")
        col_devil.write(
            " 👹 İyi niyetli görünen davranışlarla duygusal zekayı manipüle ederek çevrenizdekileri etkileme kabiliyetiniz, sizi kötü karaktere dönüştürüyor.")
        col_angel.markdown("<h1 style='text-align: center; color: cyan;'>👼🏻 ANGEL YOU 👼🏻</h1>", unsafe_allow_html=True)
        col_angel.image("img/VK/2.png", width=300)
        col_angel.write(
            " 😇 içsel bir ateşle yanarak, etrafınızdaki insanları aydınlatan bir varlık gibisiniz. ")
        col_angel.write(
            " 😇 Doğuştan gelen bağlantı kurma ve empati yeteneğiniz, insanlar arasında etkili bir lider olmanızı sağlıyor. ")
        col_angel.write(
            " 😇 Sıcak gülümseme ve içten bakışlarınız, çevrenizdeki herkesi destekleyici bir ışıkla sararak etkileyici bir varlık olduğunuzu gösteriyor.")
        ## spirit animals
        animal1, animal2 = tab_model.columns(2)
        animal1.write("# Ruh hayvanınız.. ")
        animal1.write("## 🦢TABİİ Kİ KUĞU!🦢")
        animal1.image("img/animals/images2.jpeg", width=350)
        animal2.write("## Neden?")
        animal2.write(
            "Ruh hayvanınız, kuğu gibi zarif ve sessiz, suyun yüzeyinde süzülen bir varlık. Duygusal derinlikleri temsil eden göletin etrafındaki ormanda, içsel güzellik ve değerleri saklıyor. Empati ve anlayışınız, insanlarla derin bağlar kurmanıza olanak tanıyor. Her zaman zarif ve duygusal bir rehber olarak, çevrenizdeki suyu durgun bırakarak olumlu etki bırakıyorsunuz. ")
    elif personality_type == "ISTP":
        tab_model.write("## 📌 FARKLI OLMAYA CESARET EDEBİLEN")
        tab_model.write(
            "Sizin dost canlısı ve özel bir yapınız var. Aniden spontan olabilir, arkadaşlarınız tarafından anlaşılmak zor olabilir. Sadık görünmenin yanında uyarı olmadan patlayan bir enerji biriktirir, cesur yeni alanlara ilgi duyarsınız. Kararlarınızı pratik gerçekçilik ve adil olma anlayışına dayandırırsınız. Muhtemelen en büyük sorununuz erken harekete geçme eğiliminiz, diğerlerinin de sizin gibi olduğunu varsaymanız olacak.")
        tab_model.write("## 📌 KURALLARA KARŞI GELEN ")
        tab_model.write(
            "Siz sınırlı kuralları ve duyarsız şakaları sevmezsiniz. Duygusal durumlarınızda bu sınırları ihlal etmek olumsuz sonuçlara neden olabilir. Duygularınızı anlamak zor olabilir, ancak bu sizin adil olma özelliğinizin bir sonucudur. Empati eksikliği bazen ilişkilerinizi karmaşıklaştırabilir. Siz, özgürlüğü tercih etmenize rağmen sınırlarla mücadele edersiniz. İyi anlayan arkadaşlarla çalışmak, beceriklilik, yaratıcılık ve pratik çözümleri birleştirme yeteneğinizi geliştirebilir ")
        col_devil, col_angel = tab_model.columns(2)
        col_devil.markdown("<h1 style='text-align: left; color: red;'> 👺 EVIL YOU 👺</h1>", unsafe_allow_html=True)
        col_devil.image("img/VK/1.png", width=300)
        col_devil.write(
            " 👹  Siz genellikle pratik, cesur ve bağımsızsınız.  ")
        col_devil.write(
            " 👹  Bağımsızlığınızı kötü niyetli amaçlar için kullanma potansiyeliniz var.  ")
        col_devil.write(
            " 👹 Duygusal soğukluğunuz ve anlık karar alma yeteneğiniz, empati eksikliği ve hızlı, etkili hareket etme yeteneğiyle ilişkilendirilebilir.")
        col_devil.write(
            " 👹  Çözüm odaklı yaklaşımınız ve risk alma eğiliminiz, kötü niyetli planlarınızı uygulamak için kullanılabilir.  ")
        col_angel.markdown("<h1 style='text-align: left; color: cyan;'>👼🏻 ANGEL YOU 👼🏻</h1>", unsafe_allow_html=True)
        col_angel.image("img/VK/2.png", width=300)
        col_angel.write(
            " 😇 Sorunları hızlı bir şekilde çözebilme yeteneğiniz ve cesaretiniz, sizi etkili bir kahraman yapabilir. ")
        col_angel.write(
            " 😇 Bağımsızlık ve özgürlüğünüzü olumlu amaçlar için kullanma eğiliminiz, kahramanlık görevlerine yönelmenize neden olabilir. ")
        col_angel.write(
            " 😇 Hızlı düşünme ve risk alma yetenekleriniz, acil durumlarla başa çıkarken etkili bir performans sergilemenizi sağlar.")
        col_angel.write(
            " 😇 Empati eksikliğiniz, mantıklı çözümlere odaklanmanıza katkıda bulunabilir. ")
        ## spirit animals
        animal1, animal2 = tab_model.columns(2)
        animal1.write("# Ruh hayvanınız.. ")
        animal1.write("## 🦅TABİİ Kİ KARTAL!🦅")
        animal1.image("img/animals/1800.jpeg", width=350)
        animal2.write("## Neden?")
        animal2.write(
            "Ruh hayvanınız, özgür ruhlu ve hızlı bir kartal. Yükseklerde özgürce süzülen bu kuş, bağımsızlığını ve hızını temsil eder. Kartal gibi, derinlemesine düşünce yeteneğiniz ve çevrenizi dikkatlice gözlemleme becerinizle öne çıkarsınız. Her anı değerlendirir ve hedeflerinize hızla ulaşma yeteneğiniz, kartalın yüksek uçuşunu yansıtır. Güçlü ve özgür ruhlu bir varlık olarak, etrafınızdaki dünyayı keskin bir gözle incelersiniz. ")
    elif personality_type == "ESTP":
        tab_model.write("Additional information about ESTP goes here.")
    elif personality_type == "ESFP":
        tab_model.write("Additional information about ESFP goes here.")
    elif personality_type == "INFP":
        tab_model.write("Additional information about INFP goes here.")
    elif personality_type == "INFJ":
        tab_model.write("Additional information about INFJ goes here.")
    elif personality_type == "ENFP":
        tab_model.write("## 📌 Günlük Hayatın Büyüsü ")
        tab_model.write(
            "Siz, dost canlısı ve dışa dönük bir insansınız. İlişkilerinizi zenginleştirmeye adanmış, enerji dolu bir kişiliğiniz var. Ancak, bu dış görünüşün altında, zengin ve canlı bir iç dünyaya sahipsiniz. Kendi benzersiz şeklinde, her şeyin ve herkesin bağlantılı olduğuna inanırsınız, bu bağlantıları anlamak sizi besler. Hayal gücünüz harekete geçtiğinde coşku dolusunuz, ancak projelerinizde disiplin ve tutarlılık konusunda zaman zaman zorluk yaşayabilirsiniz. ")
        tab_model.write("## 📌 EĞLENCE NEREDE SÖYLEYİN! ")
        tab_model.write(
            "Sizin hayattaki mutluluk ve zevk arayışınız sığ değil, tutkulu bir idealistten dans pistindeki özgür ruha dönüşebilir. Eğlenirken bile, başkalarıyla duygusal bağ kurmaya önem verir ve samimi, içten konuşmalar yapmak sizin için önemlidir. Duygusal zekanız ve cesaretiniz, sadece kendi hayatınızı değil, etrafınızdaki dünyayı da aydınlatır. Siz aynı zamanda yaratıcı ve çevik bir düşünce yapısına sahipsiniz, bu da size her durumda yenilikçi çözümler bulma yeteneği kazandırır. Ayrıca, başkalarının duygusal ihtiyaçlarına gösterdiğiniz özel hassasiyet ve anlayış, ilişkilerinizi güçlendirir ve sıcak bir çevre yaratmanıza olanak tanır.  ")
        col_devil, col_angel = tab_model.columns(2)
        col_devil.markdown("<h1 style='text-align: left; color: red;'> 👺 EVIL YOU 👺</h1>", unsafe_allow_html=True)
        col_devil.image("img/VK/1.png", width=300)
        col_devil.write(
            " 👹  Olumsuz amaçlar doğrultusunda, hayal gücünüz ve yaratıcılığınız, aldatma veya başkalarının zararına kullanılabilir.   ")
        col_devil.write(
            " 👹  Empati yeteneğiniz, başkalarını manipüle etme ve kendi çıkarlarınız doğrultusunda kullanma potansiyeline sahiptir.   ")
        col_devil.write(
            " 👹 Değişken doğanız, etrafınızdakileri etkilemek ve kontrol altına almak için kullanılabilir. ")
        col_devil.write(
            " 👹  Pozitif enerjiniz, başkalarını etkileme konusundaki becerinizle birleşerek, karanlık bir liderlik potansiyeli oluşturabilir.   ")
        col_angel.markdown("<h1 style='text-align: left; color: cyan;'>👼🏻 ANGEL YOU 👼🏻</h1>", unsafe_allow_html=True)
        col_angel.image("img/VK/2.png", width=300)
        col_angel.write(
            " 😇 Siz, Hayal gücü dolu bir vizyoner olarak, yaratıcı projelerde bulunma ve çevrenizdeki insanları olumlu bir şekilde etkileme yeteneğiniz var.  ")
        col_angel.write(
            " 😇 Empati ve anlayışınız, duygusal ihtiyaçları anlama konusundaki doğal yeteneklerinizle birleşiyor.  ")
        col_angel.write(
            " 😇 Değişime hızla adapte olabilme esnekliğiniz, farklı sosyal ortamlarda başarıya ulaşmanıza katkıda bulunuyor. ")
        col_angel.write(
            " 😇 Pozitif enerjiniz, zorluklarla karşılaştığınızda bile etrafınızdakilere ilham kaynağı oluyor. Grup içinde uyum sağlama ve olumlu bir katkı sunma isteğiniz, sizi melek gibi bir karakter yapar. ")
        ## spirit animals
        animal1, animal2 = tab_model.columns(2)
        animal1.write("# Ruh hayvanınız.. ")
        animal1.write("## 🦋TABİİ Kİ KELEBEK!🦋")
        animal1.image("img/animals/b077909f131c18eecace8dc9df05a750.jpg", width=350)
        animal2.write("## Neden?")
        animal2.write("Ruh hayvanınız, renkli ve özgür bir kelebek. Her bir kanadında değişiklik ve dönüşüm sembolleri taşıyarak, sürekli bir büyüme ve evrim içindesiniz. Kelebek gibi, enerjinizi çevrenizde yayarak olumlu bir etki bırakma yeteneğiniz var. Hayal gücünüz ve yaratıcılığınız, çiçekleri ziyaret eden kelebek gibi, etrafınıza güzellik ve ilham katıyor. Siz, özgürlük ve değişim arayışınızda, kelebek gibi renkli ve dikkat çekici bir varlıksınız")
    elif personality_type == "ISFP":
        tab_model.write("Additional information about ISFP goes here.")
    elif personality_type == "ENTP":
        tab_model.write("Additional information about ENTP goes here.")
    elif personality_type == "ISFJ":
        tab_model.write("Additional information about ISFJ goes here.")

    # Add more conditions for other personality types

if __name__ == "__main__":
    main()
