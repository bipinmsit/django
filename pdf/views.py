from django.http import HttpResponse
from django.conf import settings
from osgeo import gdal
from subprocess import Popen, PIPE
from django.template import loader
import os


def check_projection(request):
    pdf_file = os.path.join(settings.BASE_DIR, 'data', r'orwa-rbg-sfp-southriver-ansi-d.pdf')
    output_dir = os.path.dirname(pdf_file)
    output_file = os.path.join(output_dir, os.path.basename(pdf_file).split(".")[0]+'.tif')
    pdf_read = gdal.Open(pdf_file)
    cmd = "gdal_translate -of GTiff {} {}".format(pdf_file, output_file)

    # HttpResponse("You conversion started ...")
    p = Popen(cmd, shell=True, stdout=PIPE, stderr=PIPE)
    p.wait()

    # template = loader.get_template('myfirst.html')

    return HttpResponse('Conversion completed')
    # return HttpResponse(template.render())
