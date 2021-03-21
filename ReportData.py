class ReportDataProvider:
  
      def __init__(self, name, age):
        self.name = name
        self.age = age
        
      def printData(self):
          print(self.name)
          print(self.age)