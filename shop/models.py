from django.db import models
from django.contrib.auth.models import User
from . import helper
from django.urls import reverse
from mptt.models import MPTTModel, TreeForeignKey

class Category(MPTTModel):
    parent = TreeForeignKey('self',blank=True, null=True ,related_name='children', on_delete=models.CASCADE, verbose_name="فرزند")
    title = models.CharField(max_length=50, verbose_name="عنوان")
    slug = models.SlugField(null=False, unique=True, verbose_name="اسلاگ")

    def __str__(self):
        return self.title

    class MPTTMeta:
        order_insertion_by = ['title']

    def get_absolute_url(self):
        return reverse('category_detail', kwargs={'slug': self.slug})

    def __str__(self):                           # __str__ method elaborated later in
        full_path = [self.title]                  # post.  use __unicode__ in place of
        k = self.parent
        while k is not None:
            full_path.append(k.title)
            k = k.parent
        return ' / '.join(full_path[::-1])
    class Meta:
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی ها'




class Tag(models.Model):
    title = models.CharField(max_length=50, unique=True, verbose_name="عنوان")
    slug = models.SlugField(max_length=50, unique=True, allow_unicode=True, verbose_name="اسلاگ")
    description = models.TextField(max_length=500, null=True, blank=True, verbose_name="توضیحات")

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'برچسب'
        verbose_name_plural = 'برچسب ها'


class ImageGallery(models.Model):
    title = models.CharField(max_length=100, unique=True, verbose_name="عنوان")
    pic = models.ImageField(upload_to='upload/images', default='upload/images/no-img.jpg', verbose_name="تصویر")
    alt = models.CharField(max_length=200, null=True, blank=True, verbose_name="نام جایگزین")
    description = models.CharField(max_length=200, null=True, blank=True, verbose_name="توضیحات")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'گالری تصاویر'
        verbose_name_plural = 'گالری تصاویر'


class FileGallery(models.Model):
    title = models.CharField(max_length=100, unique=True, verbose_name="عنوان")
    file = models.FileField(upload_to='media/upload/files', verbose_name="فایل")
    description = models.CharField(max_length=200, null=True, blank=True, verbose_name="توضیحات")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'گالری فایل ها'
        verbose_name_plural = 'گالری فایل ها'


class Province(models.Model):
    title = models.CharField(max_length=100, unique=True, verbose_name="عنوان")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'استان'
        verbose_name_plural = 'استان ها'

class City(models.Model):
    title = models.CharField(max_length=100, unique=True, verbose_name="عنوان")
    province = models.ForeignKey(Province, on_delete=models.CASCADE, verbose_name="شهر")

    def __str__(self):
        return self.title
    class Meta:
        verbose_name = 'شهر'
        verbose_name_plural = 'شهر ها'

class Area(models.Model):
    title = models.CharField(max_length=100, unique=True, verbose_name="عنوان")
    province = models.ForeignKey(City, on_delete=models.CASCADE, verbose_name="استان")

    def __str__(self):
        return self.title
    class Meta:
        verbose_name = 'منطقه'
        verbose_name_plural = 'منطقه ها'

class Shop_name(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name="عنوان فروشگاه")
    descriptions = models.CharField(verbose_name=("درباره فروشگاه"), max_length=500)
    slug = models.SlugField(max_length=100, unique=True, allow_unicode=True, verbose_name="اسلاگ")

    class Meta:
        verbose_name = ( "فروشگاه")
        verbose_name_plural = ( "فروشگاه ها")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop-detail', args=[self.slug])

class page(models.Model):
    title = models.CharField(max_length=100, unique=True, verbose_name="عنوان")
    slug = models.SlugField(max_length=100, unique=True, allow_unicode=True, verbose_name="اسلاگ")
    decsription = models.TextField(max_length=300,verbose_name="مختصر توضیحات")
    writer = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="نویسنده")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('page-detail', args=[self.slug])

    class Meta:
        verbose_name = 'برگه'
        verbose_name_plural = 'برگه ها'


class Product(models.Model):
    title = models.CharField(max_length=100, unique=True, verbose_name="عنوان")
    slug = models.SlugField(max_length=100, unique=True, allow_unicode=True, verbose_name="اسلاگ")
    decsription = models.CharField(max_length=300,verbose_name="مختصر توضیحات")
    shop = models.ForeignKey("shop.Shop_name", verbose_name=("فروشگاه"), on_delete=models.CASCADE,null=True)
    content = models.TextField(verbose_name="توضیحات")
    publish_date = models.DateTimeField(auto_now_add=True, verbose_name="تاریخ انتشار")
    writer = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="نویسنده")
    tags = models.ManyToManyField(Tag, blank=True, verbose_name="برچسب")
    is_active_comment = models.BooleanField(default=False, verbose_name="فعال کردن نظرات")
    DRAFT = 1
    PUBLISHED = 2
    REOPEN = 3
    Order_state = (
        (DRAFT, 'پیش نویس'),
        (PUBLISHED, 'آماده فروش'),
        (REOPEN, 'اتمام موجودی'),
    )
    status = models.IntegerField(
        choices=Order_state,
        default=DRAFT,
    )
    price = models.DecimalField(max_digits=11, decimal_places=0, default=0, verbose_name="قیمت")
    has_discount = models.BooleanField(default=False, verbose_name="تخفیف")
    super_price = models.DecimalField(max_digits=11, decimal_places=0, default=0, null=True, blank=True, verbose_name="قیمت با تخفیف")
    EXPRESS = 1
    NORMAL = 2
    TIEPAKS = 3
    Product_transportation_class = (
        (EXPRESS, 'پست پیشتاز'),
        (NORMAL, 'پست سفارشی'),
        (TIEPAKS, 'تیپاکس'),
    )
    transportation_class = models.IntegerField(
        choices=Product_transportation_class,
        null=True,
        blank=True, 
        verbose_name="نوع ارسال"
    )
    AVAILABLE = 1
    UNAVAILABLE = 2
    Product_In_Stock = (
        (AVAILABLE, 'موجود'),
        (UNAVAILABLE, 'ناموجود'),
    )
    available_in_stock = models.IntegerField(
        choices=Product_In_Stock,
        default=AVAILABLE,
        verbose_name="وضعیت"
    )
    category = models.ManyToManyField(Category, blank=True, verbose_name="دسته بندی")
    pic = models.ImageField(upload_to='upload/product/images', default='upload/images/no-img.jpg', verbose_name="تصویر")
    summary = models.CharField(max_length=100, blank=True, verbose_name="تعداد")
    image_gallery = models.ManyToManyField(ImageGallery, blank=True, verbose_name="گالری تصاویر")
    related_product = models.ManyToManyField('self', blank=True,

                                             verbose_name="محصولات مرتبط")

    class Meta:
        ordering = ('-id',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('product-detail', args=[self.slug])

    class Meta:
        verbose_name = 'محصول'
        verbose_name_plural = 'محصولات'


class Order(models.Model):
    name = models.CharField(max_length=200, verbose_name="نام")
    family = models.CharField(max_length=200, verbose_name="نام خانوادگی")
    email = models.EmailField(max_length=200, verbose_name="ایمیل")
    mobile = models.CharField(max_length=11, verbose_name="شماره موبایل")
    address = models.TextField(max_length=500, blank=True, verbose_name="آدرس")
    order_note = models.CharField(max_length=200, blank=True, verbose_name="توضیحات")
    ATPLACE = 1
    ONLINE = 2
    Payment_types = (
        (ATPLACE, 'At place'),
        (ONLINE, 'Online'),
    )
    payment_type = models.IntegerField(
        choices=Payment_types,
        default=ONLINE,

    )
    is_accept_agreement = models.BooleanField()
    COMPLETED = 1
    CANCELED = 2
    INPROGRESS = 3
    CHECKING = 4
    PAYMENTTING = 5
    Order_statuses = (
        (COMPLETED, 'Completed'),
        (CANCELED, 'Canceled'),
        (INPROGRESS, 'In progress'),
        (CHECKING, 'Checking'),
        (PAYMENTTING, 'Paymentting'),
    )
    order_status = models.IntegerField(
        choices=Order_statuses,
        default=CHECKING,
    )
    authority = models.CharField(max_length=100, blank=True)
    refId = models.CharField(max_length=100, blank=True)
    order_date = models.DateTimeField(auto_now_add=True)
    order_update_date = models.DateTimeField(blank=True, null=True)
    count_of_allow_download = models.IntegerField(default=10)
    date_of_expire_download = models.DateTimeField(blank=True, null=True)
    random_order_id = models.IntegerField(default=helper.random_int, unique=True)
    amount = models.IntegerField(default=0, blank=True)

    def __str__(self):
        return str(self.random_order_id)

    def get_total_cost(self):
        return sum(item.get_cost for item in self.items.all)

    class Meta:
        verbose_name = 'سفارش'
        verbose_name_plural = 'سفارشات'

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    shop = models.ForeignKey(Shop_name, blank=True, null=True, on_delete=models.CASCADE)
    count = models.IntegerField()
    price = models.DecimalField(max_digits=11, decimal_places=0, default=0)

    def __str__(self):
        return ' Product:%s Name:%s ' % (self.product, self.order.family)

    def get_cost(self):
        return self.price * self.count
    get_cost.allow_tags = True
    class Meta:
        verbose_name = 'موارد سفارش'
        verbose_name_plural = 'موارد سفارشات'

class Accounting(models.Model):
    shop = models.ForeignKey(Shop_name, verbose_name=("فروشگاه"), on_delete=models.CASCADE)
    order = models.ForeignKey(OrderItem , on_delete=models.CASCADE)
    checkout = models.BooleanField(null=True)
    ammount = models.DecimalField(max_digits=11, decimal_places=0, default=0)
    def __str__(self):
        return self.shop.name
    class Meta:
        verbose_name = 'حسابداری'
        verbose_name_plural = 'حسابداری'

class PaymentLog(models.Model):
    order = models.ForeignKey(Order, on_delete=models.DO_NOTHING, verbose_name="سفارش")
    date = models.DateTimeField(auto_now_add=True, verbose_name="تاریخ")
    payment_code = models.CharField(max_length=200, unique=True, verbose_name="کد پرداخت")
    bank_tracking_code = models.CharField(max_length=200, blank=True, verbose_name="کد تراکنش بانکی")
    INITIAL = 1
    TOBANK = 2
    FROMBANK = 3
    ERROR = 4
    COMPLETE = 5
    Payment_statuses = (
        (INITIAL, 'Initial'),
        (TOBANK, 'To Bank'),
        (FROMBANK, 'From Bank'),
        (ERROR, 'Error'),
        (COMPLETE, 'پرداخت شده'),
    )
    Payment_status = models.IntegerField(
        choices=Payment_statuses,
        default=INITIAL, 
        verbose_name="وضعیت پرداخت"
    )
    message = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return 'Order Id:%s Payment Code:%s' % (self.order, self.payment_code)
    
    class Meta:
        verbose_name = 'گزارش پرداخت'
        verbose_name_plural = 'گزارش پرداخت ها'


class Comment(models.Model):
    full_name = models.CharField(max_length=200, verbose_name="نام")
    email = models.EmailField(blank=True, null=True, verbose_name="ایمیل")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="محصول")
    comment = models.TextField(max_length=500, verbose_name="نظر")
    reply = models.TextField(max_length=500, blank=True, null=True, verbose_name="پاسخ")
    is_active = models.BooleanField(default=False, verbose_name="فعال")
    date_created = models.DateTimeField(auto_now_add=True, verbose_name="تاریخ ایجاد")
    date_reply = models.DateTimeField(blank=True, null=True, verbose_name="تاریخ پاسخ")

    def __str__(self):
        return "{} from {}".format(self.comment[0:50], self.product)

    class Meta:
        verbose_name = 'نظر'
        verbose_name_plural = 'نظرات'

class slider(models.Model):
    title = models.CharField(max_length=100, unique=True, verbose_name="عنوان")
    title2 = models.CharField(max_length=100, blank=True, null=True, unique=True, verbose_name="عنوان دوم")
    link = models.CharField(max_length=100, unique=True, verbose_name="لینک")
    pic = models.ImageField(upload_to='upload/images', default='upload/images/no-img.jpg', verbose_name="تصویر")

    class Meta:
        verbose_name = 'اسلایدر'
        verbose_name_plural = 'اسلایدرها'

    def __str__(self):
        return self.title

class banner(models.Model):
    title = models.CharField(max_length=100, unique=True, verbose_name="عنوان")
    link = models.CharField(max_length=100, unique=True, verbose_name="لینک")
    pic = models.ImageField(upload_to='upload/images', default='upload/images/no-img.jpg', verbose_name="تصویر")

    class Meta:
        verbose_name = 'بنر'
        verbose_name_plural = 'بنرها'

    def __str__(self):
        return self.title
