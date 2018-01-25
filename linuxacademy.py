from splinter import Browser
import time

class laPrice(object):

    browser = Browser()
    laUrl = "https://linuxacademy.com/"
    username = "Your Linux Academy Username"
    passwd = "Your Linux Academy Password"
    planArr = []

    def login(self):

        self.browser.visit(self.laUrl)

        if self.browser.find_by_text("Log In").first.visible:
            self.browser.find_by_text("Log In").first.click()
        else:
            self.browser.find_by_css("button.btn.btn-la.hidden-lg.hidden-md").first.click()
            self.browser.find_by_text("Log In").first.click()


        time.sleep(3)

        self.browser.fill('username', self.username)
        self.browser.fill('password', self.passwd)

        self.browser.find_by_css(".auth0-lock-submit").first.click()

    def queryPrice(self):

        self.login()

        time.sleep(5)

        planCounter = 1

        f = open("laPrice.txt", "a+")

        for count in range(1,1901):
        #for this part, you may want to divide the task into few pieces
        #browser.visit int the for loop will consume memory like openning multiple tabs without
        #closing. So memory may br filled up.

            planCounter = count
            
            planUrl = "https://linuxacademy.com/cp/plan/details/id/{}"
            
            self.browser.visit(planUrl.format(planCounter))

            try:
                name = self.browser.find_by_css("span.plan-template-plan-name").first.value
                cost = self.browser.find_by_css("span.plan-details-cost").first.value
                period = self.browser.find_by_css("span.plan-period-price").first.value
                details = str(planCounter) + " " + name + " " + cost + period

            except Exception as e:
                if str(e) == 'no elements could be found with css "span.plan-template-plan-name"':
                    details = "No Plan at {}".format(planCounter)
                    

                elif str(e) == 'no elements could be found with css "span.plan-period-price"':
                    name = self.browser.find_by_css("span.plan-template-plan-name").first.value
                    cost = self.browser.find_by_css("span.plan-details-cost").first.value
                    details = str(planCounter) + " " + name + " " + cost

            #self.planArr[self.planCounter] = details

            #if int(cost) <= 200:
            #    print(self.planCounter, " ", details)

            f.write(details + "\n")

            print(details)

        f.close()


if __name__ == "__main__":
    checker = laPrice()
    checker.queryPrice()
