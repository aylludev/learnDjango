// list.js
console.log("El archivo JS se cargó correctamente.");

$(function() {
  $('#data').DataTable({
    responsive: true,
    autoWidth: false,
    destroy: true,
    deferRender: true,
    ajax: {
      url: window.location.pathname,
      type: 'POST',
      data: {
        'action': 'searchdata'
      }, // parametros
      dataSrc: ""
    },
    columns: [
      { "data": "id" },
      { "data": "name" },
      { "data": "desc" },
      { "data": "desc" },
    ],
    columnDefs: [
      {
        targets: [2],
        class: 'text-center',
        orderable: false,
        render: function(data, type, row) {
          return '<b>hola</b>';
        }
      },
    ],
    initComplete: function(settings, json) {
      alert('Tabla cargada');
    }
  });
});
