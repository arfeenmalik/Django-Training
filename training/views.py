import time
from django.db.models.query_utils import DeferredAttribute
from django.http import HttpResponse, FileResponse
from django.views import View
from django_filters.views import FilterView
from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_JUSTIFY, TA_RIGHT
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm, inch
from reportlab.platypus import Table, TableStyle, Indenter, KeepTogether, Spacer, Image
from .forms import TrainingForm
from .models import Training
from .filters import TrainingFilter
from django.shortcuts import render, redirect, get_object_or_404
from reportlab.pdfgen import canvas
from io import BytesIO
from reportlab.lib.pagesizes import letter, A4
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from io import BytesIO
from django.http import FileResponse


class GeneratePDF(View):
    def get(self, request, *args, **kwargs):
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="form_letter.pdf"'

        doc = SimpleDocTemplate(response, pagesize=A4)
                                # rightMargin=0, leftMargin=0,
                                # topMargin=0, bottomMargin=0)

        elements = []
        data = []
        headings = ['ID', 'Name', 'Training Type', 'Start Date', 'End Date', 'City', 'Street Address']
        data.append(headings)
        trainings = Training.objects.all()

        styleSheet = getSampleStyleSheet()
        styleSheet.add(ParagraphStyle(name='Right', alignment=TA_RIGHT))
        styleSheet.add(ParagraphStyle(name='Center', alignment=TA_CENTER))

        for idx,training in enumerate(trainings):
            data.append([
                Paragraph(str(idx+1), styleSheet["Center"]),
                Paragraph(training.name, styleSheet["BodyText"]),
                Paragraph(training.type.name, styleSheet["BodyText"]),
                Paragraph(str(training.date_start), styleSheet["Center"]),
                Paragraph(str(training.date_end), styleSheet["Center"]),
                Paragraph(training.city.name, styleSheet["BodyText"]),
                Paragraph(training.street_address, styleSheet["BodyText"]),
            ])

        table_style = TableStyle(
            [
                ('GRID', (0, 0), (-1, -1), 0.5, colors.black),
                ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
                ('ALIGN', (0, 0), (-1, 0), 'CENTER'),

            ])

        colWidths = [.5 * inch, 1 * inch, 1 * inch, 1 * inch, 1 * inch, 1 * inch, 1 * inch]

        t = Table(data, style=table_style, colWidths=colWidths, hAlign='LEFT')

        elements.append(t)
        # write the document to disk
        doc.build(elements)

        return response


# class GeneratePDF(View):
#     def get(self, request, *args, **kwargs):
#         # Create response object with PDF
#         response = HttpResponse(content_type='application/pdf')
#         response['Content-Disposition'] = 'attachment; filename="simple_table.pdf"'
#
#         # Create buffer to store PDF
#         buffer = BytesIO()
#
#         # Create PDF
#         doc = SimpleDocTemplate(buffer, pagesize=letter)
#         elements = []
#
#         # Define data and headings for table
#         # data = [['ID', 'Name', 'Age'], ['1', 'John Doe', '25'], ['2', 'Jane Smith', '30']]
#         # headings = ['ID', 'Name', 'Age']
#         data = []
#         headings = ['ID', 'Name', 'Training Type', 'Start Date', 'End Date', 'City', 'Street Address']
#         trainings = Training.objects.all()
#
#         for training in trainings:
#             # resource_names = [r.name for r in training.resources.all()]
#
#             data.append([
#                 training.id,
#                 training.name,
#                 training.type.name,
#                 str(training.date_start),
#                 str(training.date_end),
#                 training.city.name,
#                 training.street_address,
#                 # ', '.join(resource_names)
#             ])
#
#         # Define style for table
#         style = TableStyle([
#             ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
#             ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
#
#             ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
#
#             ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
#             ('FONTSIZE', (0, 0), (-1, 0), 14),
#             ('LEFTPADDING', (0, 0), (-1, -1), 5),  # Reduce left padding
#             ('LEFTMARGIN', (0, 0), (-1, -1), 0),  # Set left margin
#
#             ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
#             ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
#         ])
#
#         max_widths = [0.2*inch,0.9*inch,0.9*inch,0.9*inch,0.9*inch,0.9*inch,0.9*inch]
#
#         # Create table and add to elements list
#         table = Table([headings] + data, colWidths=max_widths,spaceBefore=5)
#         table.setStyle(style)
#         table.leftIndent = 0  # remove the left indentation
#
#         elements.append(table)
#         # Build PDF
#
#         doc.build(elements)
#
#         # Write PDF to response
#         pdf = buffer.getvalue()
#         buffer.close()
#         response.write(pdf)
#
#         return response


# class GeneratePDF(View):
#     def get(self, request, *args, **kwargs):
#         data = []
#         headings = ['ID', 'Name', 'Training Type', 'Start Date', 'End Date', 'City', 'Street Address']
#         trainings = Training.objects.all()
#
#         for training in trainings:
#             # resource_names = [r.name for r in training.resources.all()]
#
#             data.append([
#                 training.id,
#                 training.name,
#                 training.type.name,
#                 str(training.date_start),
#                 str(training.date_end),
#                 training.city.name,
#                 training.street_address,
#                 # ', '.join(resource_names)
#             ])
#
#         max_widths= [5,5,5,5,5,5,5]
#         # Create response object with PDF
#         response = HttpResponse(content_type='application/pdf')
#         response['Content-Disposition'] = 'attachment; filename="trainings.pdf"'
#
#         buffer = BytesIO()
#
#         # Create PDF
#         doc = SimpleDocTemplate(buffer, pagesize=letter)
#         elements = []
#
#         t = Table([headings] + data, colWidths=max_widths)
#
#         t.setStyle(TableStyle([
#             ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
#             ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
#
#             ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
#
#             ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
#             ('FONTSIZE', (0, 0), (-1, 0), 14),
#
#             ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
#             ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
#         ]))
#
#         elements.append(t)
#         doc.build(elements)
#
#         # Write PDF to response
#         pdf = buffer.getvalue()
#         buffer.close()
#         response.write(pdf)
#
#         return response


class TrainingListView(FilterView):
    model = Training
    filterset_class = TrainingFilter
    template_name = 'training/home.html'
    paginate_by = 10


def new_training(request):
    if request.method == 'POST':
        form = TrainingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = TrainingForm()
    return render(request, 'training/new_training.html', {'form': form})


def edit_training(request, pk):
    training = get_object_or_404(Training, pk=pk)
    if request.method == 'POST':
        form = TrainingForm(request.POST, instance=training)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = TrainingForm(instance=training)
    return render(request, 'training/edit_training.html', {'form': form, 'training': training})


def delete_training(request, pk):
    training = get_object_or_404(Training, pk=pk)

    if request.method == 'GET':
        training.delete()
        return redirect('home')
    else:
        return redirect('home')
