This repo demonstrates that how weak 'Reset Password Codes' 
can be guessed easily using selenium. 
This poses a special problem that knowing the 
username of victim (for a particular service/website) 
and by carefulling analyzing reset code patterns of that website the 
attacker can get access to victim's account. 

# Assumptions

1. The websites does not expires password reset code.
2. The website does not uses any mechanisms (max request hit limit is high, captchas etc) to avoid bots.
3. The attacker knows the username of the victim.
4. The victim has not implemented 2 Factor authentication.

Obviously it will take some days or may be weaks but its possible.

# How to be safe

1. If you own a website, make password reset code expire after few minutes to avoid this attack.
2. Put some mechanism to avoid bots .i.e. too many requests in very short amount of time.
3. If you are a user then take security issues related to services you use very seriously.
4. Don't ignore emails request resetting password if you think someone else initated password reset mechanism.
5. Always Use 2 Factor Authentication.

# Key take Aways

1. Use 2FA.
2. Audit your Password Reset Mechanism from security perspective. Developers some times are too lazy to implement good security on this end.


# Don't be a jerk by using this script for any malicious intent.
