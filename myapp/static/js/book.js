console.log("Hello sir i am working fine you can access now");

 const pickupDate = document.getElementById('pickupDate')
    const pickupTime = document.getElementById('pickupTime')
    
    const returnDate = document.getElementById('returnDate')
    const returnTime = document.getElementById('returnTime')
    console.log(`${pickupDate} and ${pickupTime} ${returnDate} ${returnTime}`);
    
    
    const rentPerDay = parseFloat(document.getElementById('rentPerDay').innerText)
    
    function calculateAmount() {
      if (!pickupDate.value || !pickupTime.value || !returnDate.value || !returnTime.value) {
        return
      }
    
      const start = new Date(pickupDate.value + 'T' + pickupTime.value)
    
      const end = new Date(returnDate.value + 'T' + returnTime.value)
    
      const diffMs = end - start
    
      if (diffMs <= 0) {
        alert('Return date must be greater than pickup date')
        return
      }
    
      let totalDays = Math.ceil(diffMs / (1000 * 60 * 60 * 24))
    
      let subtotal = totalDays * rentPerDay
    
      let tax = subtotal * 0.10
    
      let deposit = 2000
    
      let grandTotal = subtotal + tax + deposit
    
      document.getElementById('totalDays').innerText = totalDays
    
      document.getElementById('subtotal').innerText = subtotal.toFixed(2)
    
      document.getElementById('tax').innerText = tax.toFixed(2)
    
      document.getElementById('grandTotal').innerText = grandTotal.toFixed(2)
    }
    
    pickupDate.addEventListener('change', calculateAmount)
    
    pickupTime.addEventListener('change', calculateAmount)
    
    returnDate.addEventListener('change', calculateAmount)
    
    returnTime.addEventListener('change', calculateAmount)