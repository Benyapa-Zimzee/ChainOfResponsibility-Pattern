class SupportHandler {
    constructor(nextHandler = null) {
        this.nextHandler = nextHandler;
    }

    handle(request) {
        if (this.nextHandler) {
            this.nextHandler.handle(request);
        }
    }
}

class TeacherSupport extends SupportHandler {
    handle(request) {
        if (request === "Teacher") {
            alert("The teacher will handle your request.");
        } else {
            super.handle(request);
        }
    }
}

class HeadOfFacultySupport extends SupportHandler {
    handle(request) {
        if (request === "Head") {
            alert("The head of faculty will handle your request.");
        } else {
            super.handle(request);
        }
    }
}

class DeanSupport extends SupportHandler {
    handle(request) {
        if (request === "Dean") {
            alert("The dean will handle your request.");
        } else {
            super.handle(request);
        }
    }
}

class FinanceSupport extends SupportHandler {
    handle(request) {
        if (request === "Finance") {
            alert("The finance department will handle your request.");
        } else {
            super.handle(request);
        }
    }
}

class HRSupport extends SupportHandler {
    handle(request) {
        if (request === "HR") {
            alert("The HR department will handle your request.");
        } else {
            alert("Sorry, we don't provide support for this request.");
        }
    }
}

function handleRequest() {
    const request = document.getElementById("request").value;
    supportHandler.handle(request);
}

const hrSupport = new HRSupport();
const financeSupport = new FinanceSupport(hrSupport);
const deanSupport = new DeanSupport(financeSupport);
const headOfFacultySupport = new HeadOfFacultySupport(deanSupport);
const teacherSupport = new TeacherSupport(headOfFacultySupport);
const supportHandler = teacherSupport;
