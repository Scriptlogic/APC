class Report:
    def generate(self):
        print("Generating Report")


class PDFReport(Report):
    def generate(self):
        print("Generating PDF Report")


class ExcelReport(Report):
    def generate(self):
        print("Generating Excel Report")


class HTMLReport(Report):
    def generate(self):
        print("Generating HTML Report")


def generate_report(report):
    report.generate()


r1 = PDFReport()
generate_report(r1)

r2 = ExcelReport()
generate_report(r2)

r3 = HTMLReport()
generate_report(r3)