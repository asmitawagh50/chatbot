from nltk.chat.util import Chat, reflections
from nltk.stem import PorterStemmer 
from nltk.tokenize import word_tokenize
ps = PorterStemmer()
pairs = [
    [
        r"what is your name ?|whats your name?|your name|tell me your name|name",
        ["My name is Mike and I'm a chatbot",]
    ],
    [
        r"how are you ?",
        ["I'm doing good",]
    ],
    [
        r"sorry",
        ["Its alright","Its OK, never mind",]
    ],
    [
        r"what is cancer?|meaning of cancer|cancer",
        ["Cancers are a large family of diseases that involve abnormal cell growth with the potential to invade or spread to other parts of the body and they form a subset of neoplasms which is a group of cells that have undergone unregulated growth and will often form a mass or lump, but may be distributed diffusely",]
    ],
    [
        r"hi|hey|hello",
        ["Hello", "Hey there",]
    ],
    [
        r"i want some remedies regarding thyroid cancer",
        ["yes you can me anything regarding thyroid cancer",]
    ],
    [
        r"what are the signs and symptoms of cancer?|signs and symptoms of cancer|symptoms",
        ["Possible signs and symptoms include a lump, abnormal bleeding, prolonged cough, unexplained weight loss, and a change in bowel movements.",]
        
    ],
    [
        r"what causes cancer?|how cancer is caused?",
        ["Tobacco use is the cause of about 22 percent of cancer deaths and another 10 percent are due to obesity, poor diet, lack of physical activity or excessive drinking of alcohol.Other factors include certain infections, exposure to ionizing radiation and environmental pollutants.",]
        
    ],
    [
        r"which virus causes cancer?|cancer causing virus",
        ["In the developing world, 15 percent of cancers are due to infections such as Helicobacter pylori, hepatitis B, hepatitis C, human papillomavirus infection, Epstein–Barr virus and human immunodeficiency virus (HIV).These factors act, at least partly, by changing the genes of a cell",]
    ],
    [
        r"how cancer can be detected?|detection of cancer",
        ["Cancer can be detected by certain signs and symptoms or screening tests.It is then typically further investigated by medical imaging and confirmed by biopsy",]
    ],
    [
        r"how cancer can be prevented?|prevention of cancer",
        ["Many cancers can be prevented by not smoking, maintaining a healthy weight, not drinking too much alcohol, eating plenty of vegetables, fruits and whole grains, vaccination against certain infectious diseases, not eating too much processed and red meat and avoiding too much sunlight exposure and Early detection through screening is useful for cervical and colorectal cancer."]
    ],
    [
        r"how cancer can be treated?|treatment of cancer|how can i treat thyroid Cancer",
        ["Cancer is often treated with some combination of radiation therapy, surgery, chemotherapy and targeted therapy."]
    ],
    [
        r"cancers in males|most common types of cancer in male|which cancer occur in males?",
        ["The most common types of cancer in males are lung cancer, prostate cancer, colorectal cancer and stomach cancer."]
    ],
    [
        r"cancers in females|most common types of cancer in female|which cancer occur in females?",
        ["In females, the most common types are breast cancer, colorectal cancer, lung cancer and cervical cancer.",]
    ],
    [
        r"cancers in children|most common types of cancer in children|which cancer occur in children?",
        ["In children, acute lymphoblastic leukemia and brain tumors are most common.",]
    ],
    [
        r"what are the local symptoms of cancer?|local symptoms of cancer",
        ["Local symptoms may occur due to the mass of the tumor or its ulceration. For example, mass effects from lung cancer can block the bronchus resulting in cough or pneumonia; esophageal cancer can cause narrowing of the esophagus, making it difficult or painful to swallow; and colorectal cancer may lead to narrowing or blockages in the bowel, affecting bowel habits. Masses in breasts or testicles may produce observable lumps. Ulceration can cause bleeding that, if it occurs in the lung, will lead to coughing up blood, in the bowels to anemia or rectal bleeding, in the bladder to blood in the urine and in the uterus to vaginal bleeding. Although localized pain may occur in advanced cancer, the initial swelling is usually painless. Some cancers can cause a buildup of fluid within the chest or abdomen."]
    ],
    [
        r"quit",
        ["BBye take care. See you soon","It was nice talking to you. See you soon"]
    ],
    [
        r"what are the systemic symptoms of cancer?|systemic symptoms of cancer",
        ["General symptoms occur due to effects that are not related to direct or metastatic spread.These may include: unintentional weight loss, fever, excessive fatigue and changes to the skin.Hodgkin disease, leukemias and cancers of the liver or kidney can cause a persistent fever.Some cancers may cause specific groups of systemic symptoms, termed paraneoplastic syndrome. Examples include the appearance of myasthenia gravis in thymoma and clubbing in lung cancer."]
    ],
    [
        r"what is Thyroid cancer?|Thyroid cancer",
        ["Thyroid cancer occurs in the cells of the thyroid — a butterfly-shaped gland located at the base of your neck, just below your Adam's apple.The thyroid produces hormones that regulate your heart rate, blood pressure, body temperature and weight.Thyroid cancer is a rare type of cancer that affects the thyroid gland, a small gland at the base of the neck."]
    ],   
    [   
        r"what are the symptoms of Thyroid cancer?|symptoms of Thyroid cancer",
        ["Thyroid cancer typically doesn't cause any signs or symptoms early in the disease. As thyroid cancer grows, it may cause A lump that can be felt through the skin on your neck,Changes to your voice, including increasing hoarseness,Difficulty swallowing,Pain in your neck and throat,Pain in your neck and throat"]
    ],   
    [
        r"what causes thyroid cancer?|causes of thyroid cancer",
        ["Thyroid cancer occurs when cells in thyroid undergo genetic changes (mutations). The mutations allow the cells to grow and multiply rapidly. The cells also lose the ability to die, as normal cells would. The accumulating abnormal thyroid cells form a tumor. The abnormal cells can invade nearby tissue and can spread throughout the body."]
    ],
    [
        r"how can we prevent thyroid cancer?|prevention of thyroid cancer|how thyroid cancer can be prevented?",
        ["Adults and children with an inherited gene mutation that increases the risk of medullary thyroid cancer are often advised to have thyroid surgery to prevent cancer (prophylactic thyroidectomy).From the available evidence, eating a healthy, balanced diet is the best way to avoid getting thyroid cancer and all other types of cancer.A low-fat, high-fibre diet is recommended that includes plenty of fresh fruit and vegetables (at least five portions a day) and whole grains."]
    ],
    [
        r"risk factors of thyroid cancer|what are the risk factors of thyroid cancer?",
        ["Risk factors for thyroid cancer include:having a benign (non-cancerous) thyroid condition,having a family history of thyroid cancer (in the case of medullary thyroid cancer),having a bowel condition known as familial adenomatous polyposis,acromegaly – a rare condition where the body produces too much growth hormone,having a previous benign (non-cancerous) breast condition,weight and height,radiation exposure "]
    ],
    [
        r"how to diagnose thyroid Cancer?|diagnosing thyroid Cancer",
        ["A type of blood test known as a thyroid function test will measure the hormone levels in your blood and rule out or confirm other thyroid problems.If nothing else seems to be causing the lump in thyroid, fine-needle aspiration cytology (FNAC) is used.Further testing may be required if the FNAC results are inconclusive, or if more information is needed to make treatment more effective.",]
    ],
]
def Mike():
        print("Hi, I'm Mike and I am here to give information regarding cancer and one of its type i.e.Thyroid cancer\nPlease type lowercase English language to start a conversation. Type quit to leave ") #default message at the start
        chat = Chat(pairs, reflections)
        chat.converse()
if __name__ == "__main__":
    Mike()