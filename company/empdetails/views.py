import pymssql as pymssql
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from .Serializers import employee_serializer

server = '192.168.10.221'
database = 'testdatabase '
username = 'sa'
password = 'gitech123*'
port = '49263'

class empdetailsAPIView(APIView):
    permission_classes = (IsAuthenticated,)

    @swagger_auto_schema(request_body=employee_serializer)

    def post(self, request):
        serializer = employee_serializer(data=request.data)
        if not serializer.is_valid():
            return Response({"success:False", "errors:serializer.errors"}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
        deptno =serializer.validated_data['deptno']
        try:
            conn = pymssql.connect(server=server, user=username, password=password,
                                   database=database, port=port, autocommit=True)
            cur = conn.cursor()
            cur.execute(f"Exec EMP_DeptDetails {deptno};")
            result = cur.fetchall()
            a = []
            for n in result:
                d = {
                    "Empid": n[0],
                    "Ename": n[1],
                    "Job": n[2],
                    "Hiredate": n[3],
                    "Sal": n[4],
                    "Deptno": n[5],
                    "Currentvalues": n[6],
                }
                a.append(d)
            return Response(
                {
                    "success": True,
                    "result": a
                },
                status=status.HTTP_200_OK
            )
        except:
            raise
            conn.rollback()
        else:
            conn.commit()
        finally:
            if conn:
                cur.close()
                conn.close()
