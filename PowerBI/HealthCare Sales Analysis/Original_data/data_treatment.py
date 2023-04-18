import pandas as pd

daily=pd.read_csv('salesdaily.csv')
hourly=pd.read_csv('saleshourly.csv')
monthly=pd.read_csv('salesmonthly.csv')
weekly=pd.read_csv('salesweekly.csv')

##conversion
daily=daily.melt(id_vars='datum',value_vars=['M01AB','M01AE','N02BA','N02BE','N05B','N05C','R03','R06'],var_name='product',value_name='Sales_amount')
hourly=hourly.melt(id_vars='datum',value_vars=['M01AB','M01AE','N02BA','N02BE','N05B','N05C','R03','R06'],var_name='product',value_name='Sales_amount')
monthly=monthly.melt(id_vars='datum',value_vars=['M01AB','M01AE','N02BA','N02BE','N05B','N05C','R03','R06'],var_name='product',value_name='Sales_amount')
weekly=weekly.melt(id_vars='datum',value_vars=['M01AB','M01AE','N02BA','N02BE','N05B','N05C','R03','R06'],var_name='product',value_name='Sales_amount')


# Create a Pandas Excel writer using XlsxWriter as the engine.
writer = pd.ExcelWriter('health_sales.xlsx', engine='xlsxwriter')
daily.to_excel(writer, sheet_name='daily',index=False)
hourly.to_excel(writer, sheet_name='hourly',index=False)
monthly.to_excel(writer, sheet_name='monthly',index=False)
weekly.to_excel(writer, sheet_name='weekly',index=False)
# Close the Pandas Excel writer and output the Excel file.
writer.close()

print('Process complete....')

