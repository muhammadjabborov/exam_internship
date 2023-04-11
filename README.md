
1) **Keshlash (caching) nima va nega bizga keshlash kerak?**

Javob
# bu ma'lumotlarni o'z ichiga olgan vaqt va kuchni kamaytirish uchun ishlatiladigan avtomatik protseduradir

2) **Unit testlari nima va ular nima uchun muhim?**

Javob
# unit testining asosiy maqsadi sinash uchun yozma kodni ajratish va u maqsadga muvofiq ishlayotganligini aniqlashdir 
# yani biz unit test bilan har hil katta va kichik dasturlarni test qilsak boladi
# unit testlari bir necha sabablarga ko'ra muhimdir 
-- ular kodning moljallanganidek ishlashini taminlashga yordam beradi va har qanday xato yoki xatolar quyi oqimda yanada muhimroq muammolarni keltirib chiqarishi mumkin bolishidan oldin ishlab chiqish jarayonida erta aniqlanishiga yordam beradi bu uzoq muddatda vaqt va resurslarni tejashga yordam beradi chunki rivojlanish tsiklining boshida xatolarni tuzatish odatda osonroq va arzonroqdir -- 

3) **Django ORM da select_related va prefetch_related ning maqsadi nima va ular qanday farq qiladi?**

Javob
# select_related asosan foreign key bilan bogliq obyektlarni chaqirishda ishlatiladi. 
# prefetch_related asosan Many-to-Many, One-to-Many va reverse ForeignKey bilan bogliq modellarni chaqirishda ishlatiladi.
-- farq shundaki select_related asosan birlikda chaqiriladigan malumotlarni qollaydi prefetch_related esa bogliq bolgan malumotlarni alohida sorov orqali chaqirib olish imkonini beradi. Shuning uchun, birinchi usulning ishlatilishi tajribali ma'lumotlar soni kamida bo'lgan ishlar uchun qulaylik yaratadi, ikkinchi usul esa ko'p qatorli jadvallar bilan ishlovchi so'rovlarda yoki katta ma'lumotlar bazalari uchun ishlatiladi.