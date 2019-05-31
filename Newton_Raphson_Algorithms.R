s0 <- 34
E <- 34
r <- 0.001
t <- 1
c <- 2.7240
#Initial value of volatility:
sigma <- 0.10
sig <- rep(0,10)
sig[1] <- sigma
#Newton-Raphson method:
for(i in 2:100){
  d1 <- (log(s0/E)+(r+sigma^2/2)*t)/(sigma*sqrt(t))
  d2 <- d1-sigma*sqrt(t)
  f <- s0*pnorm(d1)-E*exp(-r*t)*pnorm(d2)-c
  #Derivative of d1 w.r.t. sigma:
  d11 <- (sigma^2*t*sqrt(t)-(log(s0/E)+(r+sigma^2/2)*t)*sqrt(t))/(sigma^2*t)
  #Derivative of d2 w.r.t. sigma:
  d22 <- d11-sqrt(t)
  #Derivative of f(sigma):
  f1 <- s0*dnorm(d1)*d11-E*exp(-r*t)*dnorm(d2)*d22
  #Update sigma:
  sigma <- sigma - f/f1
  sig[i] <- sigma
  if(abs(sig[i]-sig[i-1]) < 0.00000001){sig<- sig[1:i]; break}
}
sig