from django.shortcuts import render, redirect
from .models import User, EmergencyReport, Contact


def home(request):
    return render(request, 'home.html')


def login(request):
    if request.method == "POST":

        email = request.POST.get("email")
        password = request.POST.get("password")

        try:
            user = User.objects.get(
                email=email,
                password=password
            )

            request.session["user_id"] = user.id
            request.session["user_name"] = user.full_name

            return redirect("/dashboard/")

        except User.DoesNotExist:
            return render(request, "login.html", {
                "error": "Invalid Email or Password"
            })

    return render(request, "login.html")



def register(request):

    if request.method == "POST":

        full_name = request.POST.get("full_name")
        email = request.POST.get("email")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")


        if password == confirm_password:

            User.objects.create(
                full_name=full_name,
                email=email,
                password=password
            )

            return redirect('/login/')


    return render(request, 'register.html')



def dashboard(request):

    if "user_id" not in request.session:
        return redirect("/login/")


    total_users = User.objects.count()

    total_reports = EmergencyReport.objects.count()

    reports = EmergencyReport.objects.all().order_by("-id")


    context = {

        "total_users": total_users,

        "total_reports": total_reports,

        "reports": reports,

        "user_name": request.session["user_name"],

    }


    return render(request, "dashboard.html", context)




def report(request):

    if request.method == "POST":

        name = request.POST.get("name")

        phone = request.POST.get("phone")

        location = request.POST.get("location")

        emergency_type = request.POST.get("emergency_type")

        description = request.POST.get("description")


        EmergencyReport.objects.create(

            name=name,

            phone=phone,

            location=location,

            emergency_type=emergency_type,

            description=description

        )


        return render(request, "report.html", {

            "success": "Emergency Report Submitted Successfully!"

        })


    return render(request, "report.html")





def assistant(request):

    answer = ""


    if request.method == "POST":


        question = request.POST.get("question", "").lower()



        if "আগুন" in question or "fire" in question:

            answer = """

🔥 আগুন লাগলে করণীয়:


1. শান্ত থাকুন।

2. দ্রুত নিরাপদ স্থানে চলে যান।

3. ধোঁয়া থাকলে নিচু হয়ে চলুন।

4. Fire Service এ কল করুন: 999

"""


        elif "ভূমিকম্প" in question or "earthquake" in question:

            answer = """

🌍 ভূমিকম্প হলে করণীয়:


1. Drop, Cover, Hold করুন।

2. জানালা ও ভারী জিনিস থেকে দূরে থাকুন।

3. লিফট ব্যবহার করবেন না।

"""


        elif "সাপ" in question or "snake" in question:


            answer = """

🐍 সাপ কামড়ালে করণীয়:


1. শান্ত থাকুন।

2. আক্রান্ত স্থান কম নড়াচড়া করুন।

3. দ্রুত হাসপাতালে যান।

"""


        elif "দুর্ঘটনা" in question or "accident" in question:


            answer = """

🚑 দুর্ঘটনা হলে:


1. আহত ব্যক্তিকে নিরাপদ স্থানে রাখুন।

2. Emergency Service এ যোগাযোগ করুন।

3. দ্রুত চিকিৎসার ব্যবস্থা করুন।

"""


        else:

            answer = """

🤖 দুঃখিত, এই বিষয়ে তথ্য পাওয়া যায়নি।

আগুন, ভূমিকম্প, সাপ কামড় বা দুর্ঘটনা সম্পর্কে প্রশ্ন করুন।

"""



    return render(request, 'assistant.html', {

        "answer": answer

    })





def profile(request):

    if "user_id" not in request.session:

        return redirect("/login/")


    user = User.objects.get(
        id=request.session["user_id"]
    )


    if request.method == "POST":


        user.full_name = request.POST.get("full_name")

        user.email = request.POST.get("email")


        user.save()


        request.session["user_name"] = user.full_name


        return redirect("/profile/")



    return render(request, "profile.html", {

        "user": user

    })





def admin_dashboard(request):


    if "user_id" not in request.session:

        return redirect("/login/")



    total_users = User.objects.count()


    total_reports = EmergencyReport.objects.count()



    reports = EmergencyReport.objects.all().order_by("-id")



    emergency_data = {}



    for report in reports:


        if report.emergency_type in emergency_data:

            emergency_data[report.emergency_type] += 1


        else:

            emergency_data[report.emergency_type] = 1



    context = {


        "total_users": total_users,


        "total_reports": total_reports,


        "reports": reports,


        "chart_labels": list(emergency_data.keys()),


        "chart_data": list(emergency_data.values()),


    }



    return render(request, "admin_dashboard.html", context)


def about(request):
    return render(request, "about.html")
def contact(request):

    if request.method == "POST":

        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")

        contact.objects.create(
            name=name,
            email=email,
            message=message
        )

        return render(request, "contact.html", {
            "success": "Message Sent Successfully!"
        })

    return render(request, "contact.html")

def logout(request):

    request.session.flush()

    return redirect("/login/")