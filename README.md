# apis-re-identification
## Simple data re-identification attack through protected APIs outputs
While protected APIs act as the outer shell of data protection, ensuring secure communication and controlled access, this layer alone leaves the core exposed. Clever attackers can weave together fragments of information from multiple APIs to re-identify sensitive data.

To reinforce the inner layer, you need to consider not just what goes into the API, but also what comes out.

Let's imagine you want to find out a specific employee's salary (we'll call them the target) but the company only exposes aggregate data over protected APIs.

Despite the company's efforts to anonymize individual data within these aggregates, a determined attacker can deduce the target's salary through statistical analysis and pattern recognition:


### Step 1:
request the sum of salaries for all employees

```ruby
curl http://localhost:5000/api/total_payroll
```

### Step 2:
request the sum of salaries again, but this time excluding the target

```ruby
curl 'http://localhost:5000/api/total_payroll/exclude_criteria?age=35&department=HR'
```

### Step 3:
subtract the two sums to isolate the target's salary

---
   
This is a simplified example, but it highlights the vulnerability. Re-identification attacks can work by combining seemingly innocuous pieces of anonymized data with external information or exploiting patterns within the data itself.

That’s where Differential Privacy can help; it can be applied at the output level without altering the data, simply by adding a controlled amount of statistical noise - just enough to mask an individual’s contribution. This guarantees that the outputs cannot be combined to expose sensitive information on an individual. 




