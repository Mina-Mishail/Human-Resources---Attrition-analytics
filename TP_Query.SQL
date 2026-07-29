select 
	d.Department as Department_Name, 
	J.JobRol as Job_Role, 
	count(e.attrition)  as Total_attrition,
	AVG(e.MonthlyIncome) as Average_MonthlyIncome

	from fact_employee e with(nolock)
        Inner join dim_department d with(nolock) on e.Department_ID = d.Department_ID 
        Inner join dim_jobrole j with(nolock) on e.Role_ID = j.Role_ID 
	where e.attrition = 'Yes'
        Group by d.Department,
                 j.JobRol
		  Order By [Total_attrition] Desc ;